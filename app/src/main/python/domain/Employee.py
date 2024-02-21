from datetime import datetime
from enum import Enum
from typing import List
from . import Job
from . import JobHistory
from . import Department
from DatabaseConfig import db
 


class Employee(db.Model):
    __tablename__ = "Employee"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String( 255))
    last_name = db.Column(db.String( 255))
    email = db.Column(db.String( 255))
    phone_number = db.Column(db.String( 255))
    hire_date = db.Column(db.DateTime)
    salary = db.Column(db.Integer)
    commission_pct = db.Column(db.Integer)

    # TODO: Adding relationships
    jobs = db.relationship("Job", lazy="subquery", viewonly=True)
    manager_id = db.Column(db.Integer, db.ForeignKey("Employee.id"))    
    manager = db.relationship("Employee", lazy="subquery", primaryjoin="Employee.manager_id == Employee.id")
    department_id = db.Column(db.Integer, db.ForeignKey("Department.id"))    
    department = db.relationship("Department", lazy="subquery", primaryjoin="Employee.department_id == Department.id")

    @classmethod
    def find_by_id(cls, _id) -> "Employee":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Employee"]:
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
    
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
    
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def get_hire_date(self):
        return self.hire_date

    def set_hire_date(self, hire_date):
        self.hire_date = hire_date
    
    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary
    
    def get_commission_pct(self):
        return self.commission_pct

    def set_commission_pct(self, commission_pct):
        self.commission_pct = commission_pct
