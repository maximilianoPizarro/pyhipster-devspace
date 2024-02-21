from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Location import Location
from schema.LocationSchema import LocationSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
locations_list_ns = Namespace('locations-resource', path="/locations")

locations_schema = LocationSchema()
locations_list_schema = LocationSchema(many=True)


class LocationResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on LocationResource")
        locations = Location.find_by_id(id)
        if locations is not None:
            return locations_schema.dump(locations), 200
        return {"message": "Location not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on LocationResource")
        locations_json = request.get_json()
        if locations_json["id"] is None:
            return {"message": "Invalid Location"}, 400
        if id != locations_json["id"]:
            return {"message": "Invalid Location"}, 400
        locations = Location.find_by_id(id)
        if locations.get_id() is None:
            return {"message": "Invalid Location"}, 400
        try:
            updated_locations = locations_schema.load(locations_json, instance=locations, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_locations.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return locations_schema.dump(updated_locations), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on LocationResource")
        locations_json = request.get_json()
        if locations_json["id"] is None:
            return {"message": "Invalid Location"}, 400
        if id != locations_json["id"]:
            return {"message": "Invalid Location"}, 400
        locations = Location.find_by_id(id)
        if locations.get_id() is None:
            return {"message": "Invalid Location"}, 400
        try:
            updated_locations = locations_schema.load(locations_json, instance=locations, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_locations.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return locations_schema.dump(updated_locations), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on LocationResource")
        locations = Location.find_by_id(id)
        if locations is None:
            return {"message": "Location not found"}, 404
        try:
            locations.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Location deleted"}, 204


class LocationResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on LocationResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        locations = Location.find_all(page, size)
        if locations is not None:
            return locations_list_schema.dump(locations), 200
        return {"message": "Location not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on LocationResourceList")
        locations_json = request.get_json()
        try:
            locations_data = locations_schema.load(locations_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            locations_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return locations_schema.dump(locations_data), 201


class LocationResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on LocationResourceListCount")
        locations_count = Location.find_all_count()
        if locations_count is not None:
            return locations_count, 200
        return {"message": "Location count not found"}, 404