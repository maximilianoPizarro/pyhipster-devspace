from datetime import datetime
from enum import Enum
from typing import List
from .enumeration.OrdenStatus import OrdenStatus
from .enumeration.MetodoDePago import MetodoDePago
from . import ProductoOrden
from . import Cliente
from DatabaseConfig import db
 


class Carrito(db.Model):
    __tablename__ = "Carrito"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime, nullable=False)
    referencia = db.Column(db.String( 255))
    status = db.Column(db.Enum(OrdenStatus, nullable=False))
    metodo_de_pago = db.Column(db.Enum(MetodoDePago, nullable=False))

    # TODO: Adding relationships
    ordens = db.relationship("ProductoOrden", lazy="subquery", viewonly=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("Cliente.id"))    
    cliente = db.relationship("Cliente", lazy="subquery", primaryjoin="Carrito.cliente_id == Cliente.id")

    @classmethod
    def find_by_id(cls, _id) -> "Carrito":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Carrito"]:
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
    
    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha
    
    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
    
    def get_metodo_de_pago(self):
        return self.metodo_de_pago

    def set_metodo_de_pago(self, metodo_de_pago):
        self.metodo_de_pago = metodo_de_pago
    
    def get_referencia(self):
        return self.referencia

    def set_referencia(self, referencia):
        self.referencia = referencia
