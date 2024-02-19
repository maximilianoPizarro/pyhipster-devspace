from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Cliente import Cliente
from schema.ClienteSchema import ClienteSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
clientes_list_ns = Namespace('clientes-resource', path="/clientes")

clientes_schema = ClienteSchema()
clientes_list_schema = ClienteSchema(many=True)


class ClienteResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on ClienteResource")
        clientes = Cliente.find_by_id(id)
        if clientes is not None:
            return clientes_schema.dump(clientes), 200
        return {"message": "Cliente not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on ClienteResource")
        clientes_json = request.get_json()
        if clientes_json["id"] is None:
            return {"message": "Invalid Cliente"}, 400
        if id != clientes_json["id"]:
            return {"message": "Invalid Cliente"}, 400
        clientes = Cliente.find_by_id(id)
        if clientes.get_id() is None:
            return {"message": "Invalid Cliente"}, 400
        try:
            updated_clientes = clientes_schema.load(clientes_json, instance=clientes, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_clientes.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return clientes_schema.dump(updated_clientes), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on ClienteResource")
        clientes_json = request.get_json()
        if clientes_json["id"] is None:
            return {"message": "Invalid Cliente"}, 400
        if id != clientes_json["id"]:
            return {"message": "Invalid Cliente"}, 400
        clientes = Cliente.find_by_id(id)
        if clientes.get_id() is None:
            return {"message": "Invalid Cliente"}, 400
        try:
            updated_clientes = clientes_schema.load(clientes_json, instance=clientes, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_clientes.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return clientes_schema.dump(updated_clientes), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on ClienteResource")
        clientes = Cliente.find_by_id(id)
        if clientes is None:
            return {"message": "Cliente not found"}, 404
        try:
            clientes.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Cliente deleted"}, 204


class ClienteResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ClienteResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        clientes = Cliente.find_all(page, size)
        if clientes is not None:
            return clientes_list_schema.dump(clientes), 200
        return {"message": "Cliente not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on ClienteResourceList")
        clientes_json = request.get_json()
        try:
            clientes_data = clientes_schema.load(clientes_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            clientes_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return clientes_schema.dump(clientes_data), 201


class ClienteResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ClienteResourceListCount")
        clientes_count = Cliente.find_all_count()
        if clientes_count is not None:
            return clientes_count, 200
        return {"message": "Cliente count not found"}, 404