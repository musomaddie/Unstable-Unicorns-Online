""" grid location dataclass. """
from dataclasses import dataclass


@dataclass
class GridPosition:
    """ Stores a pair of values corresponding to a location in a grid. Each value defaults to zero"""
    row: int = 0
    col: int = 0
