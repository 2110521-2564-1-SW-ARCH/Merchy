from enum import Enum

class Courier(str, Enum):
    THPOST = "thpost"

class Platform(str, Enum):
    LAZADA = "lazada"