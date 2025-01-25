# Interpreter that does boolean operations and normal arithmetic
# Module imports for processing
from dataclasses import dataclass
#from midiutil import MIDIFile
type LiteralVal = int | bool
type ExpressionType = Add | Sub | Mul | Div | Neg | Lit | Let | Name | And | Or | Not | Eq | Lt | If
# Integer Literal Arithmetic
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
# Boolean Arithmetic
@dataclass 
class And():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} && {self.right_val})"
@dataclass 
class Or():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} || {self.right_val})"
@dataclass
class Not():
    subexpression: ExpressionType
    def __str__(self) -> str:
        return f"(NOT {self.subexpression})"
@dataclass
class Eq():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} == {self.right_val})"
@dataclass
class Lt():
    left_val:ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} < {self.right_val})"
@dataclass
class If():
    condition: ExpressionType
    then_sect: ExpressionType
    else_sect: ExpressionType
    def __str__(self) -> str:
        return f"(if {self.condition} \n\tthen {self.then_sect} \n\telse {self.else_sect})"
# Value Declaration and name assignment
@dataclass
class Lit():
    value: LiteralVal
    def __str__(self) -> str:
        return f"{self.value}"
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
from typing import Any
blank_env: Environment[Any] = ()
def extend_environment[V](name: str, value: V, env: Environment[V]) -> Environment[V]:
    return ((name, value),) + env
def lookup_environment[V](name: str, env: Environment[V]) -> (V | None):
    match env:
        case ((n, v), *rest):
            if n == name:
                return v
            else:
                return lookup_environment(name, rest)
        case _:
            return None
class evaluate_error(Exception):
    pass
type blank = int | bool
def eval(e: ExpressionType) -> blank:
    return evalInEnv(blank_env, e)
def evalInEnv(env: Environment[blank], e: ExpressionType) -> blank:
    match e:
        # environment implementation for integer arithmetic
        case Add(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (int(lv), int(rv)):
                    return lv + rv
                case _:
                    raise evaluate_error("addition of non-integer values")
        case Sub(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (int(lv), int(rv)):
                    return lv - rv
                case _:
                    raise evaluate_error("subtraction of non-integer values")
        case Mul(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (int(lv), int(rv)):
                    return lv * rv
                case _:
                    raise evaluate_error("multiplication of non-integer values")
        case Div(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (int(lv), int(rv)):
                    if rv == 0:
                        raise evaluate_error("division by zero")
                    return lv // rv
                case _:
                    raise evaluate_error("division of non-integer values")                
        case Neg(s):
            match evalInEnv(env,s):
                case int(i):
                    return -i
                case _:
                    raise evaluate_error("negation of non-integer value")
        # environment implementation of boolean arithmetic
        case And(left_val, right_val):
            match (evalInEnv(env, left_val), evalInEnv(env, right_val)):
                case (bool(lv), bool(rv)):
                    return lv and rv
                case _:
                    raise evaluate_error("AND comparison of non-boolean values")
        case Or(left_val, right_val):
            match (evalInEnv(env, left_val), evalInEnv(env, right_val)):
                case (bool(lv), bool(rv)):
                    return lv or rv
                case _:
                    raise evaluate_error("OR comparison of non-boolean values")
        case Not(subexpression):
            match (evalInEnv(env, subexpression)):
                case (bool(i)):
                    return not i
                case _:
                    raise evaluate_error("NOT transformation of a non-boolean value")
        case Eq(left_val, right_val):
            match (evalInEnv(env, left_val), evalInEnv(env, right_val)):
                case (bool(lv), bool(rv)):
                    return lv == rv
                case _:
                    raise evaluate_error("EQ comparison of non-boolean values")
        case Lt(left_val, right_val):
            match (evalInEnv(env, left_val), evalInEnv(env, right_val)):
                case (int(lv), int(rv)):
                    return lv < rv
                case _:
                    raise evaluate_error("LT comparison of non-integer values")        
        case If(condition, then_sect, else_sect):
            match (evalInEnv(env, condition)):
                case (bool(c)):
                    if c:
                        return evalInEnv(env, then_sect)
                    else:
                        return evalInEnv(env, else_sect)
                case _:
                    raise evaluate_error("IF condition of a non-boolean value")
        # environment implementation of let and binding
        case Lit(lit) :
            match lit:  # two-level matching keeps type-checker happy
                case int(i):
                    return i
        case Name(n):
            v = lookup_environment(n, env)
            if v is None:
                raise evaluate_error(f"unbound name {n}")
            return v
        case Let(n,d,b):
            v = evalInEnv(env, d)
            newEnv = extend_environment(n, v, env)
            return evalInEnv(newEnv, b)
def run(e: ExpressionType) -> None:
    print(f"running: {e}")
    try:
        match eval(e):
            case int(i):
                print(f"result: {i}")
    except evaluate_error as err:
        print(err)