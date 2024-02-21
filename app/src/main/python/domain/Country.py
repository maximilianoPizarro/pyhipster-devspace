from datetime import datetime
from enum import Enum
from typing import List
from . import Region
from . import Location
from DatabaseConfig import db
 


class Country(db.Model):
    __tablename__ = "Country"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String( 255))

    # TODO: Adding relationships
    region_id = db.Column(db.Integer, db.ForeignKey("Region.id"))
    region = db.relationship("Region", lazy="subquery", primaryjoin="Country.region_id == Region.id")

    @classmethod
    def find_by_id(cls, _id) -> "Country":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Country"]:
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
    
    def get_country_name(self):
        return self.country_name

    def set_country_name(self, country_name):
        self.country_name = country_name
