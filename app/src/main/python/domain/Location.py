from datetime import datetime
from enum import Enum
from typing import List
from . import Country
from . import Department
from DatabaseConfig import db
 


class Location(db.Model):
    __tablename__ = "Location"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_address = db.Column(db.String( 255))
    postal_code = db.Column(db.String( 255))
    city = db.Column(db.String( 255))
    state_province = db.Column(db.String( 255))

    # TODO: Adding relationships
    country_id = db.Column(db.Integer, db.ForeignKey("Country.id"))
    country = db.relationship("Country", lazy="subquery", primaryjoin="Location.country_id == Country.id")

    @classmethod
    def find_by_id(cls, _id) -> "Location":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Location"]:
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
    
    def get_street_address(self):
        return self.street_address

    def set_street_address(self, street_address):
        self.street_address = street_address
    
    def get_postal_code(self):
        return self.postal_code

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code
    
    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city
    
    def get_state_province(self):
        return self.state_province

    def set_state_province(self, state_province):
        self.state_province = state_province
