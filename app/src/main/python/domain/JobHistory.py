from datetime import datetime
from enum import Enum
from typing import List
from .enumeration.Language import Language
from . import Job
from . import Department
from . import Employee
from DatabaseConfig import db
 


class JobHistory(db.Model):
    __tablename__ = "JobHistory"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    language = db.Column(db.Enum(Language))

    # TODO: Adding relationships
    job_id = db.Column(db.Integer, db.ForeignKey("Job.id"))
    job = db.relationship("Job", lazy="subquery", primaryjoin="JobHistory.job_id == Job.id")
    department_id = db.Column(db.Integer, db.ForeignKey("Department.id"))
    department = db.relationship("Department", lazy="subquery", primaryjoin="JobHistory.department_id == Department.id")
    employee_id = db.Column(db.Integer, db.ForeignKey("Employee.id"))
    employee = db.relationship("Employee", lazy="subquery", primaryjoin="JobHistory.employee_id == Employee.id")

    @classmethod
    def find_by_id(cls, _id) -> "JobHistory":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["JobHistory"]:
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
    
    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date
    
    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date
    
    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language
