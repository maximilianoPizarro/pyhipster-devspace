from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.ProductoOrden import ProductoOrden
from schema.ProductoSchema import ProductoSchema
from schema.CarritoSchema import CarritoSchema


class ProductoOrdenSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoOrden
        load_instance = True
        exclude = (
        )
        sqla_session = db.session
        
    producto = fields.Nested("ProductoSchema", required=True)
    cart = fields.Nested("CarritoSchema", required=True)
