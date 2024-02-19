from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Producto import Producto
from schema.ProductoCategoriaSchema import ProductoCategoriaSchema


class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True
        exclude = (
            "image_content_type", 
        )
        sqla_session = db.session
        
    imageContentType = auto_field("image_content_type")  
    productoCategoria = fields.Nested("ProductoCategoriaSchema", required=True)
