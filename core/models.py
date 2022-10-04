

from dataclasses import dataclass, field, fields
from typing import List

from loguru import logger

@dataclass
class Task():
    name: str = field(metadata={'alias': 'Name'}, default=None)
    siblings: bool = field(metadata={'alias': 'Siblings'}, default=None)
    mother: str = field(metadata={'alias': 'Mother'}, default=None)
    father: str = field(metadata={'alias': 'Father'}, default=None)
    siblings_by_mother: List[str] = field(metadata={'alias': 'Siblings by mother'}, default=None)
    owner: str = field(metadata={'alias': 'Owner'}, default=None)
    owner_species: str = field(metadata={'alias': 'Species'}, default=None)
    species_occupation: str = field(metadata={'alias': 'Occupation'}, default=None)
    occupation_class: str = field(metadata={'alias': 'Class'}, default=None)
    occupation_subclass: str = field(metadata={'alias': 'Subclass'}, default=None)

    def get_name_by_alias(self, alias):
        for item in fields(self):
            print(item.metadata['alias'])
            if item.metadata['alias'] == alias:
                return item.name
        
        raise ValueError(f'Не удалось найти псевдоним {alias}')
        