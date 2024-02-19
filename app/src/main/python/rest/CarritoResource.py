from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Carrito import Carrito
from schema.CarritoSchema import CarritoSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
carritos_list_ns = Namespace('carritos-resource', path="/carritos")

carritos_schema = CarritoSchema()
carritos_list_schema = CarritoSchema(many=True)


class CarritoResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on CarritoResource")
        carritos = Carrito.find_by_id(id)
        if carritos is not None:
            return carritos_schema.dump(carritos), 200
        return {"message": "Carrito not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on CarritoResource")
        carritos_json = request.get_json()
        if carritos_json["id"] is None:
            return {"message": "Invalid Carrito"}, 400
        if id != carritos_json["id"]:
            return {"message": "Invalid Carrito"}, 400
        carritos = Carrito.find_by_id(id)
        if carritos.get_id() is None:
            return {"message": "Invalid Carrito"}, 400
        try:
            updated_carritos = carritos_schema.load(carritos_json, instance=carritos, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_carritos.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return carritos_schema.dump(updated_carritos), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on CarritoResource")
        carritos_json = request.get_json()
        if carritos_json["id"] is None:
            return {"message": "Invalid Carrito"}, 400
        if id != carritos_json["id"]:
            return {"message": "Invalid Carrito"}, 400
        carritos = Carrito.find_by_id(id)
        if carritos.get_id() is None:
            return {"message": "Invalid Carrito"}, 400
        try:
            updated_carritos = carritos_schema.load(carritos_json, instance=carritos, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_carritos.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return carritos_schema.dump(updated_carritos), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on CarritoResource")
        carritos = Carrito.find_by_id(id)
        if carritos is None:
            return {"message": "Carrito not found"}, 404
        try:
            carritos.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Carrito deleted"}, 204


class CarritoResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on CarritoResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        carritos = Carrito.find_all(page, size)
        if carritos is not None:
            return carritos_list_schema.dump(carritos), 200
        return {"message": "Carrito not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on CarritoResourceList")
        carritos_json = request.get_json()
        try:
            carritos_data = carritos_schema.load(carritos_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            carritos_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return carritos_schema.dump(carritos_data), 201


class CarritoResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on CarritoResourceListCount")
        carritos_count = Carrito.find_all_count()
        if carritos_count is not None:
            return carritos_count, 200
        return {"message": "Carrito count not found"}, 404