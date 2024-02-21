from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.JobHistory import JobHistory
from schema.JobHistorySchema import JobHistorySchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
job_histories_list_ns = Namespace('job-histories-resource', path="/job-histories")

job_histories_schema = JobHistorySchema()
job_histories_list_schema = JobHistorySchema(many=True)


class JobHistoryResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on JobHistoryResource")
        job_histories = JobHistory.find_by_id(id)
        if job_histories is not None:
            return job_histories_schema.dump(job_histories), 200
        return {"message": "JobHistory not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on JobHistoryResource")
        job_histories_json = request.get_json()
        if job_histories_json["id"] is None:
            return {"message": "Invalid JobHistory"}, 400
        if id != job_histories_json["id"]:
            return {"message": "Invalid JobHistory"}, 400
        job_histories = JobHistory.find_by_id(id)
        if job_histories.get_id() is None:
            return {"message": "Invalid JobHistory"}, 400
        try:
            updated_job_histories = job_histories_schema.load(job_histories_json, instance=job_histories, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_job_histories.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return job_histories_schema.dump(updated_job_histories), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on JobHistoryResource")
        job_histories_json = request.get_json()
        if job_histories_json["id"] is None:
            return {"message": "Invalid JobHistory"}, 400
        if id != job_histories_json["id"]:
            return {"message": "Invalid JobHistory"}, 400
        job_histories = JobHistory.find_by_id(id)
        if job_histories.get_id() is None:
            return {"message": "Invalid JobHistory"}, 400
        try:
            updated_job_histories = job_histories_schema.load(job_histories_json, instance=job_histories, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_job_histories.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return job_histories_schema.dump(updated_job_histories), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on JobHistoryResource")
        job_histories = JobHistory.find_by_id(id)
        if job_histories is None:
            return {"message": "JobHistory not found"}, 404
        try:
            job_histories.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "JobHistory deleted"}, 204


class JobHistoryResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on JobHistoryResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        job_histories = JobHistory.find_all(page, size)
        if job_histories is not None:
            return job_histories_list_schema.dump(job_histories), 200
        return {"message": "JobHistory not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on JobHistoryResourceList")
        job_histories_json = request.get_json()
        try:
            job_histories_data = job_histories_schema.load(job_histories_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            job_histories_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return job_histories_schema.dump(job_histories_data), 201


class JobHistoryResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on JobHistoryResourceListCount")
        job_histories_count = JobHistory.find_all_count()
        if job_histories_count is not None:
            return job_histories_count, 200
        return {"message": "JobHistory count not found"}, 404