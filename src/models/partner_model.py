from sqlalchemy import Column, String, DateTime, Integer
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID, ARRAY


class PartnerModel(Base):
    __tablename__ = 'partner'
    user = Column(UUID(as_uuid=True), primary_key=True,  nullable=False)
    name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    age = Column(Integer(), nullable=False)
    profession =  Column(String(), nullable=False)
    license =  Column(String(), nullable=False)
    country_birth =  Column(String(), nullable=False)
    city_birth =  Column(String(), nullable=False)
    country_residence =  Column(String(), nullable=False)
    city_residence =  Column(String(), nullable=False)
    sports = Column(ARRAY(String), nullable=False)
    companies = Column(ARRAY(String), nullable=False)
    type_services = Column(ARRAY(String), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone.utc) )
    update_at = Column(DateTime(), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc) )