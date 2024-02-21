from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.JobHistory import JobHistory
from schema.JobSchema import JobSchema
from schema.DepartmentSchema import DepartmentSchema
from schema.EmployeeSchema import EmployeeSchema


class JobHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = JobHistory
        load_instance = True
        exclude = (
            "start_date", 
            "end_date", 
        )
        sqla_session = db.session
        
    startDate = auto_field("start_date") 
    endDate = auto_field("end_date") 
    job = fields.Nested("JobSchema", required=False)
    department = fields.Nested("DepartmentSchema", required=False)
    employee = fields.Nested("EmployeeSchema", required=False)
