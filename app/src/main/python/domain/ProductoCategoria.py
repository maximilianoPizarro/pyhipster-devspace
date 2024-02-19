from datetime import datetime
from enum import Enum
from typing import List
from . import Producto
from DatabaseConfig import db
 


class ProductoCategoria(db.Model):
    __tablename__ = "ProductoCategoria"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String( 255), nullable=False)
    description = db.Column(db.String( 255))

    # TODO: Adding relationships
    productos = db.relationship("Producto", lazy="subquery", viewonly=True)

    @classmethod
    def find_by_id(cls, _id) -> "ProductoCategoria":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["ProductoCategoria"]:
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
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
