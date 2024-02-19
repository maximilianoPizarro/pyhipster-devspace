from datetime import datetime
from enum import Enum
from typing import List
from .enumeration.Genero import Genero
from . import User
from . import Carrito
from DatabaseConfig import db
 


class Cliente(db.Model):
    __tablename__ = "Cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telefono = db.Column(db.String( 255), nullable=False)
    direccion_1 = db.Column(db.String( 255), nullable=False)
    direccion_2 = db.Column(db.String( 255))
    ciudad = db.Column(db.String( 255), nullable=False)
    pais = db.Column(db.String( 255), nullable=False)
    genero = db.Column(db.Enum(Genero, nullable=False))

    # TODO: Adding relationships
    user_id = db.Column(db.Integer, db.ForeignKey("jhi_user.id"))
    user = db.relationship("User", lazy="subquery", primaryjoin="Cliente.user_id == User.id")
    carts = db.relationship("Carrito", lazy="subquery", viewonly=True)

    @classmethod
    def find_by_id(cls, _id) -> "Cliente":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Cliente"]:
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
    
    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero
    
    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono
    
    def get_direccion_1(self):
        return self.direccion_1

    def set_direccion_1(self, direccion_1):
        self.direccion_1 = direccion_1
    
    def get_direccion_2(self):
        return self.direccion_2

    def set_direccion_2(self, direccion_2):
        self.direccion_2 = direccion_2
    
    def get_ciudad(self):
        return self.ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    
    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais
