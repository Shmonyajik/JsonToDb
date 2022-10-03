from __future__ import annotations

from typing import List, Optional, Union

from loguru import logger
from pydantic import BaseModel, root_validator, validator, Field

@dataclass
class Task:
    name: str
    siblings: bool = None
    mother: str = None
    father: str = None
    siblings_by_mother: list[str] | str = None
    owner: str = None
    owner_species: str = Field(None, alias='species')
    species_occupation: str = Field(None, alias='occupation')
    occupation_class: str = Field(None, alias='a_class')
    occupation_subclass: str = Field(None, alias='subclass')

    # @validator('siblings', pre=True)
    # def value_should_be_bool(cls, value):
    #     if value is not False and value is not None:
    #         logger.info(f"Значение поля siblings {value} сохранено как True")
    #         value = True
    #     return value
    
    # @root_validator(pre=True)
    # def validate(cls, values):
        
    #     return values
    # class Config:
    #     validate_assignment = True

# task = Task(name = 'Denis', siblings='Roma')
# print(task)


class Field3(BaseModel):
    id: int
    type: str
    name: str
    value: str


class Field2(BaseModel):
    id: int
    type: str
    name: str
    value: Union[str, List[str]]
    fields: Optional[List[Field3]] = None


class Field1(BaseModel):
    id: int
    type: str
    name: str
    value: Optional[str]
    fields: Optional[List[Field2]] = None


class Field(BaseModel):
    id: int
    type: str
    name: str
    value: Union[bool, str]
    fields: Optional[List[Field1]] = None

    

class TaskItem(BaseModel):
    id: int
    creation_date: str
    cancel_date: str
    fields: List[Field]


class Model(BaseModel):
    task: List[TaskItem]


