from marshmallow_sqlalchemy import auto_field, fields
from WebSerializer import ma
from DatabaseConfig import db
from domain.Cliente import Cliente
from schema.UserSchema import UserSchema


class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        load_instance = True
        exclude = (
            "direccion_1", 
            "direccion_2", 
        )
        sqla_session = db.session
        
    direccion1 = auto_field("direccion_1") 
    direccion2 = auto_field("direccion_2") 
    user = fields.Nested("UserSchema", required=True)
