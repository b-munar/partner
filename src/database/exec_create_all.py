from src.database.base import Base
from src.database.engine import engine

from src.models.partner_model import PartnerModel

table_objects = [PartnerModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )