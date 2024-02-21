from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Country import Country
from schema.RegionSchema import RegionSchema


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True
        exclude = (
            "country_name", 
        )
        sqla_session = db.session
        
    countryName = auto_field("country_name") 
    region = fields.Nested("RegionSchema", required=False)
