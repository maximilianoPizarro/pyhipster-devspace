from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Task import Task
from schema.TaskSchema import TaskSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
tasks_list_ns = Namespace('tasks-resource', path="/tasks")

tasks_schema = TaskSchema()
tasks_list_schema = TaskSchema(many=True)


class TaskResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on TaskResource")
        tasks = Task.find_by_id(id)
        if tasks is not None:
            return tasks_schema.dump(tasks), 200
        return {"message": "Task not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on TaskResource")
        tasks_json = request.get_json()
        if tasks_json["id"] is None:
            return {"message": "Invalid Task"}, 400
        if id != tasks_json["id"]:
            return {"message": "Invalid Task"}, 400
        tasks = Task.find_by_id(id)
        if tasks.get_id() is None:
            return {"message": "Invalid Task"}, 400
        try:
            updated_tasks = tasks_schema.load(tasks_json, instance=tasks, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_tasks.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return tasks_schema.dump(updated_tasks), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on TaskResource")
        tasks_json = request.get_json()
        if tasks_json["id"] is None:
            return {"message": "Invalid Task"}, 400
        if id != tasks_json["id"]:
            return {"message": "Invalid Task"}, 400
        tasks = Task.find_by_id(id)
        if tasks.get_id() is None:
            return {"message": "Invalid Task"}, 400
        try:
            updated_tasks = tasks_schema.load(tasks_json, instance=tasks, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_tasks.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return tasks_schema.dump(updated_tasks), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on TaskResource")
        tasks = Task.find_by_id(id)
        if tasks is None:
            return {"message": "Task not found"}, 404
        try:
            tasks.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Task deleted"}, 204


class TaskResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on TaskResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        tasks = Task.find_all(page, size)
        if tasks is not None:
            return tasks_list_schema.dump(tasks), 200
        return {"message": "Task not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on TaskResourceList")
        tasks_json = request.get_json()
        try:
            tasks_data = tasks_schema.load(tasks_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            tasks_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return tasks_schema.dump(tasks_data), 201


class TaskResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on TaskResourceListCount")
        tasks_count = Task.find_all_count()
        if tasks_count is not None:
            return tasks_count, 200
        return {"message": "Task count not found"}, 404