from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Job import Job
from schema.TaskSchema import TaskSchema
from schema.EmployeeSchema import EmployeeSchema


class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True
        exclude = (
            "job_title", 
            "min_salary", 
            "max_salary", 
        )
        sqla_session = db.session
        
    jobTitle = auto_field("job_title") 
    minSalary = auto_field("min_salary") 
    maxSalary = auto_field("max_salary") 
    tasks = fields.Nested("TaskSchema", many=True, required=False)
    employee = fields.Nested("EmployeeSchema", required=False)
