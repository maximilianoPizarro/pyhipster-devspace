from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Country import Country
from schema.CountrySchema import CountrySchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
countries_list_ns = Namespace('countries-resource', path="/countries")

countries_schema = CountrySchema()
countries_list_schema = CountrySchema(many=True)


class CountryResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on CountryResource")
        countries = Country.find_by_id(id)
        if countries is not None:
            return countries_schema.dump(countries), 200
        return {"message": "Country not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on CountryResource")
        countries_json = request.get_json()
        if countries_json["id"] is None:
            return {"message": "Invalid Country"}, 400
        if id != countries_json["id"]:
            return {"message": "Invalid Country"}, 400
        countries = Country.find_by_id(id)
        if countries.get_id() is None:
            return {"message": "Invalid Country"}, 400
        try:
            updated_countries = countries_schema.load(countries_json, instance=countries, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_countries.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return countries_schema.dump(updated_countries), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on CountryResource")
        countries_json = request.get_json()
        if countries_json["id"] is None:
            return {"message": "Invalid Country"}, 400
        if id != countries_json["id"]:
            return {"message": "Invalid Country"}, 400
        countries = Country.find_by_id(id)
        if countries.get_id() is None:
            return {"message": "Invalid Country"}, 400
        try:
            updated_countries = countries_schema.load(countries_json, instance=countries, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_countries.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return countries_schema.dump(updated_countries), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on CountryResource")
        countries = Country.find_by_id(id)
        if countries is None:
            return {"message": "Country not found"}, 404
        try:
            countries.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Country deleted"}, 204


class CountryResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on CountryResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        countries = Country.find_all(page, size)
        if countries is not None:
            return countries_list_schema.dump(countries), 200
        return {"message": "Country not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on CountryResourceList")
        countries_json = request.get_json()
        try:
            countries_data = countries_schema.load(countries_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            countries_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return countries_schema.dump(countries_data), 201


class CountryResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on CountryResourceListCount")
        countries_count = Country.find_all_count()
        if countries_count is not None:
            return countries_count, 200
        return {"message": "Country count not found"}, 404