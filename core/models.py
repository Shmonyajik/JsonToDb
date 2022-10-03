

from typing import List, Optional, Union

from loguru import logger
from pydantic import BaseModel, root_validator, validator, Field


class Task(BaseModel):
    name: str = None
    siblings: bool = None
    mother: str = None
    father: str = None
    siblingsbymother: Union[str, List[str]] = Field(None, alias='siblings_by_mother')
    owner: str = None
    species: str = Field(None, alias='owner_species')
    occupation: str = Field(None, alias='species_occupation')
    a_class : str = Field(None, alias='occupation_class')
    subclass: str = Field(None, alias='occupation_subclass')

   
    @validator('father')
    def validate(cls, value):
        logger.info("Вызвалось")
        if value == None:
            logger.info(f"{cls}")
            value = "False"
        return value

    class Config:
        validate_assignment = True


