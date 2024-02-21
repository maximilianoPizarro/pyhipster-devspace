from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Job import Job
from schema.JobSchema import JobSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
jobs_list_ns = Namespace('jobs-resource', path="/jobs")

jobs_schema = JobSchema()
jobs_list_schema = JobSchema(many=True)


class JobResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on JobResource")
        jobs = Job.find_by_id(id)
        if jobs is not None:
            return jobs_schema.dump(jobs), 200
        return {"message": "Job not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on JobResource")
        jobs_json = request.get_json()
        if jobs_json["id"] is None:
            return {"message": "Invalid Job"}, 400
        if id != jobs_json["id"]:
            return {"message": "Invalid Job"}, 400
        jobs = Job.find_by_id(id)
        if jobs.get_id() is None:
            return {"message": "Invalid Job"}, 400
        try:
            updated_jobs = jobs_schema.load(jobs_json, instance=jobs, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_jobs.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return jobs_schema.dump(updated_jobs), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on JobResource")
        jobs_json = request.get_json()
        if jobs_json["id"] is None:
            return {"message": "Invalid Job"}, 400
        if id != jobs_json["id"]:
            return {"message": "Invalid Job"}, 400
        jobs = Job.find_by_id(id)
        if jobs.get_id() is None:
            return {"message": "Invalid Job"}, 400
        try:
            updated_jobs = jobs_schema.load(jobs_json, instance=jobs, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_jobs.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return jobs_schema.dump(updated_jobs), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on JobResource")
        jobs = Job.find_by_id(id)
        if jobs is None:
            return {"message": "Job not found"}, 404
        try:
            jobs.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Job deleted"}, 204


class JobResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on JobResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        jobs = Job.find_all(page, size)
        if jobs is not None:
            return jobs_list_schema.dump(jobs), 200
        return {"message": "Job not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on JobResourceList")
        jobs_json = request.get_json()
        try:
            jobs_data = jobs_schema.load(jobs_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            jobs_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return jobs_schema.dump(jobs_data), 201


class JobResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on JobResourceListCount")
        jobs_count = Job.find_all_count()
        if jobs_count is not None:
            return jobs_count, 200
        return {"message": "Job count not found"}, 404