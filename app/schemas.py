import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("Loading Pydantic schemas.")

class ResourceBase(BaseModel):
    name: str = Field(..., example="Tela Health Remote Consultation")
    description: str = Field(..., example="Provides telehealth services in remote Florida areas")
    category: str = Field(..., example="Tela Health")
    location: str = Field(..., example="Pensacola, FL")

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    class Config:
        orm_mode = True

logger.info("Pydantic schemas loaded.")
