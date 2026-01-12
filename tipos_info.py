"""
TIPOS DE INFORMAÇÃO
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""

frase = "Olá pessoal!"
num_int = 58
num_float = 100.5
complexo = 1j
lista01 = ["João", "Maria", "José"]
tupla01 = ("A", "B")
range01 = range(6)
dicionario = {"nome": "William", "age": 28}
setup = {"A", "B", "C"}
frozen = frozenset({"A", "B", "C"})
booleano = bool(5)
bytes01 = bytes(5)
byte_array = bytearray(5)
memory_view = memoryview(bytes(5))

from datetime import datetime

data = datetime.today().date()
