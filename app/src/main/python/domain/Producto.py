from datetime import datetime
from enum import Enum
from typing import List
from .enumeration.Medida import Medida
from . import ProductoCategoria
from . import ProductoOrden
from DatabaseConfig import db
 


class Producto(db.Model):
    __tablename__ = "Producto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String( 255), nullable=False)
    description = db.Column(db.String( 255))
    image = db.Column(db.String)
    image_content_type = db.Column(db.String)    
    medida = db.Column(db.Enum(Medida, nullable=False))

    # TODO: Adding relationships
    productoCategoria_id = db.Column(db.Integer, db.ForeignKey("ProductoCategoria.id"))    
    productoCategoria = db.relationship("ProductoCategoria", lazy="subquery", primaryjoin="Producto.productoCategoria_id == ProductoCategoria.id")
    productoOrdens = db.relationship("ProductoOrden", lazy="subquery", viewonly=True)

    @classmethod
    def find_by_id(cls, _id) -> "Producto":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Producto"]:
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
    
    def get_medida(self):
        return self.medida

    def set_medida(self, medida):
        self.medida = medida
    
    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
