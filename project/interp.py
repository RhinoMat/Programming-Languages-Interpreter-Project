# Interpreter that does boolean operations and normal arithmetic
# Module imports for processing
from dataclasses import dataclass
from typing import Any
type ExpressionType = Add | Sub | Mul | Div | Neg | Lit | Let | Name
@dataclass
class Add():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} + {self.right_val})"
@dataclass
class Sub():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} - {self.right_val})"
@dataclass
class Mul():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} * {self.right_val})"
@dataclass
class Div():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} / {self.right_val})"
@dataclass
class Neg():
    subexpression: ExpressionType
    def __str__(self) -> str:
        return f"(- {self.subexpression})"
@dataclass
class Lit():
    value: int
    def __str__(self) -> str:
        return f"(- {self.subexpression})"
@dataclass
class Let():
    var_name: str
    defexpr: ExpressionType
    bodyexpr: ExpressionType
    def __str__(self) -> str:
        return f"(let {self.var_name} = {self.defexpr} in {self.bodyexpr})"
@dataclass
class Name():
    var_name: str
    def __str__(self) -> str:
        return self.var_name

type Bind[V] = tuple[str, V]
type Environment[V] = tuple[Bind[V], ...]
