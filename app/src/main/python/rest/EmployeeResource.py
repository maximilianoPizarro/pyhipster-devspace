from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Employee import Employee
from schema.EmployeeSchema import EmployeeSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
employees_list_ns = Namespace('employees-resource', path="/employees")

employees_schema = EmployeeSchema()
employees_list_schema = EmployeeSchema(many=True)


class EmployeeResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on EmployeeResource")
        employees = Employee.find_by_id(id)
        if employees is not None:
            return employees_schema.dump(employees), 200
        return {"message": "Employee not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on EmployeeResource")
        employees_json = request.get_json()
        if employees_json["id"] is None:
            return {"message": "Invalid Employee"}, 400
        if id != employees_json["id"]:
            return {"message": "Invalid Employee"}, 400
        employees = Employee.find_by_id(id)
        if employees.get_id() is None:
            return {"message": "Invalid Employee"}, 400
        try:
            updated_employees = employees_schema.load(employees_json, instance=employees, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_employees.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return employees_schema.dump(updated_employees), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on EmployeeResource")
        employees_json = request.get_json()
        if employees_json["id"] is None:
            return {"message": "Invalid Employee"}, 400
        if id != employees_json["id"]:
            return {"message": "Invalid Employee"}, 400
        employees = Employee.find_by_id(id)
        if employees.get_id() is None:
            return {"message": "Invalid Employee"}, 400
        try:
            updated_employees = employees_schema.load(employees_json, instance=employees, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_employees.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return employees_schema.dump(updated_employees), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on EmployeeResource")
        employees = Employee.find_by_id(id)
        if employees is None:
            return {"message": "Employee not found"}, 404
        try:
            employees.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Employee deleted"}, 204


class EmployeeResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on EmployeeResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        employees = Employee.find_all(page, size)
        if employees is not None:
            return employees_list_schema.dump(employees), 200
        return {"message": "Employee not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on EmployeeResourceList")
        employees_json = request.get_json()
        try:
            employees_data = employees_schema.load(employees_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            employees_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return employees_schema.dump(employees_data), 201


class EmployeeResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on EmployeeResourceListCount")
        employees_count = Employee.find_all_count()
        if employees_count is not None:
            return employees_count, 200
        return {"message": "Employee count not found"}, 404