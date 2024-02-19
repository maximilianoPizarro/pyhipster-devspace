from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.ProductoCategoria import ProductoCategoria
from schema.ProductoCategoriaSchema import ProductoCategoriaSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
producto_categorias_list_ns = Namespace('producto-categorias-resource', path="/producto-categorias")

producto_categorias_schema = ProductoCategoriaSchema()
producto_categorias_list_schema = ProductoCategoriaSchema(many=True)


class ProductoCategoriaResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on ProductoCategoriaResource")
        producto_categorias = ProductoCategoria.find_by_id(id)
        if producto_categorias is not None:
            return producto_categorias_schema.dump(producto_categorias), 200
        return {"message": "ProductoCategoria not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on ProductoCategoriaResource")
        producto_categorias_json = request.get_json()
        if producto_categorias_json["id"] is None:
            return {"message": "Invalid ProductoCategoria"}, 400
        if id != producto_categorias_json["id"]:
            return {"message": "Invalid ProductoCategoria"}, 400
        producto_categorias = ProductoCategoria.find_by_id(id)
        if producto_categorias.get_id() is None:
            return {"message": "Invalid ProductoCategoria"}, 400
        try:
            updated_producto_categorias = producto_categorias_schema.load(producto_categorias_json, instance=producto_categorias, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_producto_categorias.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_categorias_schema.dump(updated_producto_categorias), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on ProductoCategoriaResource")
        producto_categorias_json = request.get_json()
        if producto_categorias_json["id"] is None:
            return {"message": "Invalid ProductoCategoria"}, 400
        if id != producto_categorias_json["id"]:
            return {"message": "Invalid ProductoCategoria"}, 400
        producto_categorias = ProductoCategoria.find_by_id(id)
        if producto_categorias.get_id() is None:
            return {"message": "Invalid ProductoCategoria"}, 400
        try:
            updated_producto_categorias = producto_categorias_schema.load(producto_categorias_json, instance=producto_categorias, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_producto_categorias.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_categorias_schema.dump(updated_producto_categorias), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on ProductoCategoriaResource")
        producto_categorias = ProductoCategoria.find_by_id(id)
        if producto_categorias is None:
            return {"message": "ProductoCategoria not found"}, 404
        try:
            producto_categorias.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "ProductoCategoria deleted"}, 204


class ProductoCategoriaResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoCategoriaResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        producto_categorias = ProductoCategoria.find_all(page, size)
        if producto_categorias is not None:
            return producto_categorias_list_schema.dump(producto_categorias), 200
        return {"message": "ProductoCategoria not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on ProductoCategoriaResourceList")
        producto_categorias_json = request.get_json()
        try:
            producto_categorias_data = producto_categorias_schema.load(producto_categorias_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            producto_categorias_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return producto_categorias_schema.dump(producto_categorias_data), 201


class ProductoCategoriaResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on ProductoCategoriaResourceListCount")
        producto_categorias_count = ProductoCategoria.find_all_count()
        if producto_categorias_count is not None:
            return producto_categorias_count, 200
        return {"message": "ProductoCategoria count not found"}, 404