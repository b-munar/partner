from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.partner_model import PartnerModel
from src.schemas.partner_schema import PartnerDeserializeSchema, PartnerSerializeSchema
from src.utils.authorization import authorization

class PartnerController(Resource):
    method_decorators = [authorization]
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
        partner_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_partner = PartnerModel(**partner_create_dump)
        session.add(new_partner)
        session.commit()

        partner_created_schema = PartnerSerializeSchema()
        partner_created_dump = partner_created_schema.dump(new_partner)
        return partner_created_dump, 201
    
    def get(self, **kwargs):
        partner_schema = PartnerSerializeSchema()

        session = Session()
        query = session.query(PartnerModel).filter(PartnerModel.user==kwargs["user"]["id"])
        session.close()
        
        partners = [partner_schema.dump(partner) for partner in query]
        return partners, 200

