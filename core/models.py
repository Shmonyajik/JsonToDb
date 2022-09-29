from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Union

from loguru import logger
from pydantic import BaseModel, validator

@dataclass
class Task:
    name: str
    siblings: bool = None
    mother: str = None
    father: str = None
    siblings_by_mother: list[str] | str = None
    owner: str = None
    owner_species: str = None
    species_occupation: str = None
    occupation_class: str = None
    occupation_subclass: str = None

    @validator('siblings')
    def value_should_be_bool(cls, s):
        if s is not bool and s is not None:
            logger.info(f"поле value со значением {s} сохраненно как True")
            s = True
        return s


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


