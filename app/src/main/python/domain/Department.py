from datetime import datetime
from enum import Enum
from typing import List
from . import Location
from . import Employee
from . import JobHistory
from DatabaseConfig import db
 


class Department(db.Model):
    __tablename__ = "Department"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String( 255), nullable=False)

    # TODO: Adding relationships
    location_id = db.Column(db.Integer, db.ForeignKey("Location.id"))
    location = db.relationship("Location", lazy="subquery", primaryjoin="Department.location_id == Location.id")
    employees = db.relationship("Employee", lazy="subquery", viewonly=True)

    @classmethod
    def find_by_id(cls, _id) -> "Department":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Department"]:
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
    
    def get_department_name(self):
        return self.department_name

    def set_department_name(self, department_name):
        self.department_name = department_name
