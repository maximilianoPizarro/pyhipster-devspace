from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Employee import Employee
from schema.DepartmentSchema import DepartmentSchema


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
        exclude = (
            "first_name", 
            "last_name", 
            "phone_number", 
            "hire_date", 
            "commission_pct", 
        )
        sqla_session = db.session
        
    firstName = auto_field("first_name") 
    lastName = auto_field("last_name") 
    phoneNumber = auto_field("phone_number") 
    hireDate = auto_field("hire_date") 
    commissionPct = auto_field("commission_pct") 
    manager = fields.Nested("EmployeeSchema", required=False)
    department = fields.Nested("DepartmentSchema", required=False)
