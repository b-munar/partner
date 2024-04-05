from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.partner_model import PartnerModel
from src.schemas.partner_schema import PartnerDeserializeSchema, PartnerSerializeSchema
from src.utils.authorization import authorization

class PartnerController(Resource):
    method_decorators = {'get': [authorization]}
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        partner_create_schema = PartnerDeserializeSchema()
        
        errors = partner_create_schema.validate(request_json)
        if errors:
            return "", 400
        
        partner_create_dump = partner_create_schema.dump(request_json)

        session = Session()
        new_partner = PartnerModel(**partner_create_dump)
        session.add(new_partner)
        session.commit()

        partner_created_schema = PartnerSerializeSchema()
        partner_created_dump = partner_created_schema.dump(new_partner)
        return {"partner": partner_created_dump}, 201
    
    def get(self, **kwargs):
        partner_schema = PartnerSerializeSchema()

        session = Session()
        query = session.query(PartnerModel).filter(PartnerModel.user==kwargs["user"]["id"]).one()
        session.close()
        
        return {"partner": partner_schema.dump(query)}, 200

