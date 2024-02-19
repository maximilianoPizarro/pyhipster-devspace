from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Producto import Producto
from schema.ProductoSchema import ProductoSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
productos_list_ns = Namespace('productos-resource', path="/productos")

productos_schema = ProductoSchema()
productos_list_schema = ProductoSchema(many=True)


class ProductoResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on ProductoResource")
        productos = Producto.find_by_id(id)
        if productos is not None:
            return productos_schema.dump(productos), 200
        return {"message": "Producto not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on ProductoResource")
        productos_json = request.get_json()
        if productos_json["id"] is None:
            return {"message": "Invalid Producto"}, 400
        if id != productos_json["id"]:
            return {"message": "Invalid Producto"}, 400
        productos = Producto.find_by_id(id)
        if productos.get_id() is None:
            return {"message": "Invalid Producto"}, 400
        try:
            updated_productos = productos_schema.load(productos_json, instance=productos, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_productos.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return productos_schema.dump(updated_productos), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on ProductoResource")
        productos_json = request.get_json()
        if productos_json["id"] is None:
            return {"message": "Invalid Producto"}, 400
        if id != productos_json["id"]:
            return {"message": "Invalid Producto"}, 400
        productos = Producto.find_by_id(id)
        if productos.get_id() is None:
            return {"message": "Invalid Producto"}, 400
        try:
            updated_productos = productos_schema.load(productos_json, instance=productos, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_productos.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return productos_schema.dump(updated_productos), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on ProductoResource")
        productos = Producto.find_by_id(id)
        if productos is None:
            return {"message": "Producto not found"}, 404
        try:
            productos.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Producto deleted"}, 204


class ProductoResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        productos = Producto.find_all(page, size)
        if productos is not None:
            return productos_list_schema.dump(productos), 200
        return {"message": "Producto not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on ProductoResourceList")
        productos_json = request.get_json()
        try:
            productos_data = productos_schema.load(productos_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            productos_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return productos_schema.dump(productos_data), 201


class ProductoResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoResourceListCount")
        productos_count = Producto.find_all_count()
        if productos_count is not None:
            return productos_count, 200
        return {"message": "Producto count not found"}, 404