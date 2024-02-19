from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Carrito import Carrito
from schema.ClienteSchema import ClienteSchema


class CarritoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Carrito
        load_instance = True
        exclude = (
            "metodo_de_pago",
        )
        sqla_session = db.session
        
    metodoDePago = auto_field("metodo_de_pago") 
    cliente = fields.Nested("ClienteSchema", required=True)
