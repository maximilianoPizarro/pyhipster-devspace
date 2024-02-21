from datetime import datetime
from enum import Enum
from typing import List
from . import Country
from DatabaseConfig import db
 


class Region(db.Model):
    __tablename__ = "Region"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    region_name = db.Column(db.String( 255))

    # TODO: Adding relationships

    @classmethod
    def find_by_id(cls, _id) -> "Region":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Region"]:
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
    
    def get_region_name(self):
        return self.region_name

    def set_region_name(self, region_name):
        self.region_name = region_name
