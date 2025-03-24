import logging
from sqlalchemy.orm import Session
from app.models import Resource
from app.schemas import ResourceCreate

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_resources(db: Session, skip: int = 0, limit: int = 100) -> list[Resource]:
    """
    Retrieve a list of healthcare resources from the database.
    """
    logger.debug(f"Fetching resources with skip={skip} and limit={limit}.")
    resources = db.query(Resource).offset(skip).limit(limit).all()
    logger.info(f"Retrieved {len(resources)} resources from the database.")
    return resources

def create_resource(db: Session, resource: ResourceCreate) -> Resource:
    """
    Create a new healthcare resource in the database.
    """
    logger.debug(f"Creating resource with name: {resource.name}.")
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    logger.info(f"Resource '{db_resource.name}' created with ID {db_resource.id}.")
    return db_resource
