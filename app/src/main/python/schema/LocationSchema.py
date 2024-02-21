from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Location import Location
from schema.CountrySchema import CountrySchema


class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        load_instance = True
        exclude = (
            "street_address", 
            "postal_code", 
            "state_province", 
        )
        sqla_session = db.session
        
    streetAddress = auto_field("street_address") 
    postalCode = auto_field("postal_code") 
    stateProvince = auto_field("state_province") 
    country = fields.Nested("CountrySchema", required=False)
