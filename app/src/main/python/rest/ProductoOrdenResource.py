from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.ProductoOrden import ProductoOrden
from schema.ProductoOrdenSchema import ProductoOrdenSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
producto_ordens_list_ns = Namespace('producto-ordens-resource', path="/producto-ordens")

producto_ordens_schema = ProductoOrdenSchema()
producto_ordens_list_schema = ProductoOrdenSchema(many=True)


class ProductoOrdenResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on ProductoOrdenResource")
        producto_ordens = ProductoOrden.find_by_id(id)
        if producto_ordens is not None:
            return producto_ordens_schema.dump(producto_ordens), 200
        return {"message": "ProductoOrden not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on ProductoOrdenResource")
        producto_ordens_json = request.get_json()
        if producto_ordens_json["id"] is None:
            return {"message": "Invalid ProductoOrden"}, 400
        if id != producto_ordens_json["id"]:
            return {"message": "Invalid ProductoOrden"}, 400
        producto_ordens = ProductoOrden.find_by_id(id)
        if producto_ordens.get_id() is None:
            return {"message": "Invalid ProductoOrden"}, 400
        try:
            updated_producto_ordens = producto_ordens_schema.load(producto_ordens_json, instance=producto_ordens, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_producto_ordens.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_ordens_schema.dump(updated_producto_ordens), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on ProductoOrdenResource")
        producto_ordens_json = request.get_json()
        if producto_ordens_json["id"] is None:
            return {"message": "Invalid ProductoOrden"}, 400
        if id != producto_ordens_json["id"]:
            return {"message": "Invalid ProductoOrden"}, 400
        producto_ordens = ProductoOrden.find_by_id(id)
        if producto_ordens.get_id() is None:
            return {"message": "Invalid ProductoOrden"}, 400
        try:
            updated_producto_ordens = producto_ordens_schema.load(producto_ordens_json, instance=producto_ordens, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_producto_ordens.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_ordens_schema.dump(updated_producto_ordens), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on ProductoOrdenResource")
        producto_ordens = ProductoOrden.find_by_id(id)
        if producto_ordens is None:
            return {"message": "ProductoOrden not found"}, 404
        try:
            producto_ordens.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "ProductoOrden deleted"}, 204


class ProductoOrdenResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoOrdenResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        producto_ordens = ProductoOrden.find_all(page, size)
        if producto_ordens is not None:
            return producto_ordens_list_schema.dump(producto_ordens), 200
        return {"message": "ProductoOrden not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on ProductoOrdenResourceList")
        producto_ordens_json = request.get_json()
        try:
            producto_ordens_data = producto_ordens_schema.load(producto_ordens_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            producto_ordens_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_ordens_schema.dump(producto_ordens_data), 201


class ProductoOrdenResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoOrdenResourceListCount")
        producto_ordens_count = ProductoOrden.find_all_count()
        if producto_ordens_count is not None:
            return producto_ordens_count, 200
        return {"message": "ProductoOrden count not found"}, 404