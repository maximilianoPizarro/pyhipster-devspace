from datetime import datetime
from enum import Enum
from typing import List
from . import Producto
from . import Carrito
from DatabaseConfig import db
 


class ProductoOrden(db.Model):
    __tablename__ = "ProductoOrden"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cantidad = db.Column(db.Integer, nullable=False)

    # TODO: Adding relationships
    producto_id = db.Column(db.Integer, db.ForeignKey("Producto.id"))    
    producto = db.relationship("Producto", lazy="subquery", primaryjoin="ProductoOrden.producto_id == Producto.id")
    cart_id = db.Column(db.Integer, db.ForeignKey("Carrito.id"))    
    cart = db.relationship("Carrito", lazy="subquery", primaryjoin="ProductoOrden.cart_id == Carrito.id")

    @classmethod
    def find_by_id(cls, _id) -> "ProductoOrden":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["ProductoOrden"]:
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
    
    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
