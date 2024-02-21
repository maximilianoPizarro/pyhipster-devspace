from datetime import datetime
from enum import Enum
from typing import List
from . import Task
from . import JobHistory
from . import Employee
from DatabaseConfig import db
 

job_task = db.Table('job_task',
    db.Column('job_id', db.Integer, db.ForeignKey('Job.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('Task.id'), primary_key=True)
)

class Job(db.Model):
    __tablename__ = "Job"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String( 255))
    min_salary = db.Column(db.Integer)
    max_salary = db.Column(db.Integer)

    # TODO: Adding relationships
    tasks = db.relationship("Task", secondary=job_task, lazy="subquery")
    employee_id = db.Column(db.Integer, db.ForeignKey("Employee.id"))    
    employee = db.relationship("Employee", lazy="subquery", primaryjoin="Job.employee_id == Employee.id")

    @classmethod
    def find_by_id(cls, _id) -> "Job":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Job"]:
        paginate = cls.query.order_by(cls.id).paginate(page=page, per_page=per_page)
        return paginate.items

    @classmethod
    def find_all_count(cls):
        return cls.query.count()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update_db(self) -> None:
        db.session.merge(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    # Getters and setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title
    
    def get_min_salary(self):
        return self.min_salary

    def set_min_salary(self, min_salary):
        self.min_salary = min_salary
    
    def get_max_salary(self):
        return self.max_salary

    def set_max_salary(self, max_salary):
        self.max_salary = max_salary
