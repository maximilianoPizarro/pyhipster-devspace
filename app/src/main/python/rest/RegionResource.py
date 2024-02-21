from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from domain.Region import Region
from schema.RegionSchema import RegionSchema
from flask_jwt_extended import jwt_required
from security.SecurityUtils import has_role
from security.AuthoritiesConstants import AuthoritiesConstants
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
regions_list_ns = Namespace('regions-resource', path="/regions")

regions_schema = RegionSchema()
regions_list_schema = RegionSchema(many=True)


class RegionResource(Resource):
    @jwt_required()
    def get(self, id):
        logging.info("GET request received on RegionResource")
        regions = Region.find_by_id(id)
        if regions is not None:
            return regions_schema.dump(regions), 200
        return {"message": "Region not found"}, 404

    @jwt_required()
    def put(self, id):
        logging.info("PUT request received on RegionResource")
        regions_json = request.get_json()
        if regions_json["id"] is None:
            return {"message": "Invalid Region"}, 400
        if id != regions_json["id"]:
            return {"message": "Invalid Region"}, 400
        regions = Region.find_by_id(id)
        if regions.get_id() is None:
            return {"message": "Invalid Region"}, 400
        try:
            updated_regions = regions_schema.load(regions_json, instance=regions, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_regions.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return regions_schema.dump(updated_regions), 200
    
    @jwt_required()
    def patch(self, id):
        logging.info("PATCH request received on RegionResource")
        regions_json = request.get_json()
        if regions_json["id"] is None:
            return {"message": "Invalid Region"}, 400
        if id != regions_json["id"]:
            return {"message": "Invalid Region"}, 400
        regions = Region.find_by_id(id)
        if regions.get_id() is None:
            return {"message": "Invalid Region"}, 400
        try:
            updated_regions = regions_schema.load(regions_json, instance=regions, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_regions.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return regions_schema.dump(updated_regions), 200

    @jwt_required()
    @has_role(AuthoritiesConstants.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on RegionResource")
        regions = Region.find_by_id(id)
        if regions is None:
            return {"message": "Region not found"}, 404
        try:
            regions.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return {"message": "Region deleted"}, 204


class RegionResourceList(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on RegionResourceList")
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=20, type=int)
        regions = Region.find_all(page, size)
        if regions is not None:
            return regions_list_schema.dump(regions), 200
        return {"message": "Region not found"}, 404

    @jwt_required()
    def post(self):
        logging.info("POST request received on RegionResourceList")
        regions_json = request.get_json()
        try:
            regions_data = regions_schema.load(regions_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            regions_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__['orig'])}, 400
        return regions_schema.dump(regions_data), 201


class RegionResourceListCount(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on RegionResourceListCount")
        regions_count = Region.find_all_count()
        if regions_count is not None:
            return regions_count, 200
        return {"message": "Region count not found"}, 404