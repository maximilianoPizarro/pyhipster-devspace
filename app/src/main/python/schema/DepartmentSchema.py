from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Department import Department
from schema.LocationSchema import LocationSchema


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True
        exclude = (
            "department_name", 
        )
        sqla_session = db.session
        
    departmentName = auto_field("department_name") 
    location = fields.Nested("LocationSchema", required=False)
