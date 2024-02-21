from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Region import Region


class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        load_instance = True
        exclude = (
            "region_name", 
        )
        sqla_session = db.session
        
    regionName = auto_field("region_name") 
