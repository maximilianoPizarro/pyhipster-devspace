from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.ProductoCategoria import ProductoCategoria


class ProductoCategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoCategoria
        load_instance = True
        exclude = (
        )
        sqla_session = db.session
        
