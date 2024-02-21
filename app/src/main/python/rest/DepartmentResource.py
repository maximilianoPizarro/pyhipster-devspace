from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Department import Department
from schema.DepartmentSchema import DepartmentSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
departments_list_ns = Namespace('departments-resource', path="/departments")

departments_schema = DepartmentSchema()
departments_list_schema = DepartmentSchema(many=True)


class DepartmentResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on DepartmentResource")
        departments = Department.find_by_id(id)
        if departments is not None:
            return departments_schema.dump(departments), 200
        return {"message": "Department not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on DepartmentResource")
        departments_json = request.get_json()
        if departments_json["id"] is None:
            return {"message": "Invalid Department"}, 400
        if id != departments_json["id"]:
            return {"message": "Invalid Department"}, 400
        departments = Department.find_by_id(id)
        if departments.get_id() is None:
            return {"message": "Invalid Department"}, 400
        try:
            updated_departments = departments_schema.load(departments_json, instance=departments, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_departments.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return departments_schema.dump(updated_departments), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on DepartmentResource")
        departments_json = request.get_json()
        if departments_json["id"] is None:
            return {"message": "Invalid Department"}, 400
        if id != departments_json["id"]:
            return {"message": "Invalid Department"}, 400
        departments = Department.find_by_id(id)
        if departments.get_id() is None:
            return {"message": "Invalid Department"}, 400
        try:
            updated_departments = departments_schema.load(departments_json, instance=departments, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_departments.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return departments_schema.dump(updated_departments), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on DepartmentResource")
        departments = Department.find_by_id(id)
        if departments is None:
            return {"message": "Department not found"}, 404
        try:
            departments.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Department deleted"}, 204


class DepartmentResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on DepartmentResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        departments = Department.find_all(page, size)
        if departments is not None:
            return departments_list_schema.dump(departments), 200
        return {"message": "Department not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on DepartmentResourceList")
        departments_json = request.get_json()
        try:
            departments_data = departments_schema.load(departments_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            departments_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return departments_schema.dump(departments_data), 201


class DepartmentResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on DepartmentResourceListCount")
        departments_count = Department.find_all_count()
        if departments_count is not None:
            return departments_count, 200
        return {"message": "Department count not found"}, 404