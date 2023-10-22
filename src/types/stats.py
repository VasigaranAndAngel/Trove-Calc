from __future__ import annotations
from enum import Enum


class Stats(Enum):
    # Main Stats
    PHYSICAL_DAMAGE = 'stats_physical_damage'
    MAGIC_DAMAGE = 'stats_magic_damage'
    MAXIMUM_HEALTH = 'stats_maximum_health'
    MAXIMUM_ENERGY = 'stats_maximum_energy'
    HEALTH_REGEN = 'stats_health_regen'
    ENERGY_REGEN = 'stats_energy_regen'
    STABILITY = 'stats_stability'
    MOVEMENT_SPEED = 'stats_movement_speed'
    ATTACK_SPEED = 'stats_attack_speed'
    JUMP = 'stats_jump'
    CRITICAL_HIT = 'stats_critical_hit'
    CRITICAL_DAMAGE = 'stats_critical_damage'
    SUPERSTITION = 'stats_superstition'
    MAGIC_FIND = 'stats_magic_find'
    LASERMANCY = 'stats_lasermancy'
    CRAFTING_SPEED = 'stats_crafting_speed'
    FLASK_CAPACITY = 'stats_flask_capacity'
    EXPERIENCE_GAIN = 'stats_experience_gain'
    BATTLE_FACTOR = 'stats_battle_factor'
    LIGHT = 'stats_light'
    CHAOS_FACTOR = 'stats_chaos_factor'
    BATTLE_BOX_DROP_RATE = 'stats_battle_box_drop_rate'
    
    # Wings and Ships
    GLIDE = 'stats_glide'
    TURNING_RATE = 'stats_turning_rate'
    ACCELERATION = 'stats_acceleration'
    
    # Others
    DARKNESS = 'stats_darkness'
    KNOCKBACK = 'stats_knockback'
    
    
    def __str__(self) -> str:
        return f"Stats.{self.name}"
    
    def __repr__(self) -> str:
        return f"Stats.{self.name}"


class StatStack(tuple[Stats, ...]):
    """Just an inheritance of tuple for store and access Stack of Stats easily.
    So works the same as tuple."""
    def __new__(cls, *stats: Stats):
        return super().__new__(cls, stats)
