from dataclasses import dataclass

from types.gem_types import GemTypes, Variants
from types.levels import Levels
from types.rarities import Rarities
from types.stats import StatStack
from types.stars import Stars

class BaseData:
    def get_coefficient(self):
        pass
    
    def get_efficacy_ratio(self):
        pass


@dataclass
class Gem(BaseData):
    rarity: Rarities
    gem_type: GemTypes
    variant: Variants
    level: Levels
    star: Stars
    states: StatStack