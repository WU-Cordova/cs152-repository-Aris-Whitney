import copy
from dataclasses import dataclass
from enum import Enum
import random

class Suit(Enum):
    HEARTS = "❤️"
    SPADE = "♠️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class Face(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    def face_value(self) -> int:
        match self:
            case Face.JACK | Face.QUEEN | Face.KING:
                return 10
            case Face.ACE:
                return 11
            case _:
                return int(self.value)

@dataclass
class Card:
    face: Face
    suit: Suit

    def __hash__(self) -> int:
        return hash(self.face.name) * hash(self.suit.name)

    def __str__(self) -> str:
        return f"[{self.face.value}{self.suit.value}]"