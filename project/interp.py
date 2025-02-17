# Interpreter that does boolean operations and normal arithmetic
# Module imports for processing
# dataclasses automatically create initializers for marked classes
from dataclasses import dataclass
# LiteralVal marks the classes that can be utilized for literal or plain values
type LiteralVal = int | bool | str
# ExpressionType marks the available functions to utilize for the interpreter AST
type ExpressionType = Add | Sub | Mul | Div | Neg | Lit | Let | Name | And | Or | Not | Eq | NEq | Lt | LtE | Gt | GtE | If | Append | Replace | Letfun | App
# Integer Literal Arithmetic
# Add() accepts 2 integers for addition
# ex: 4 + 5 = 9
# ex: Add(Lit(4), Lit(5)) = 9
@dataclass
class Add():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} + {self.right_val})"
# Sub() accepts 2 integers for subtraction
# ex: 6 - 5 = 1
# ex: Sub(Lit(6), Lit(5)) = 1
@dataclass
class Sub():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} - {self.right_val})"
# Mul() accepts 2 integers for multiplication
# ex: 7 * 8 = 56 
# ex: Mul(Lit(7), Lit(8)) = 56
@dataclass
class Mul():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} * {self.right_val})"
# Div() accepts 2 integers for division
# throws an error upon 0 denominator
# ex: 6 / 2 = 3
# ex: Div(Lit(6), Lit(2)) = 3
@dataclass
class Div():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} / {self.right_val})"
# Neg() accepts 1 integer for negation
# flips the value of a positive to a negative and vice versa
# ex: Neg(Lit(6)) = -6
@dataclass
class Neg():
    subexpression: ExpressionType
    def __str__(self) -> str:
        return f"(- {self.subexpression})"
# Boolean Arithmetic
# And() accepts 2 booleans for the and comparison
# ex: True && False = False
# ex: And(Lit(True), Lit(False)) = False
@dataclass 
class And():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} && {self.right_val})"
# Or() accepts 2 booleans for the or comparison
# ex: True || False = True
# ex: Or(Lit(True), Lit(False)) = True
@dataclass 
class Or():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} || {self.right_val})"
# Not() accepts 1 boolean and flips from True to False and vice versa
# ex: !True = False
# ex: Not(Lit(True)) = False
@dataclass
class Not():
    subexpression: ExpressionType
    def __str__(self) -> str:
        return f"(NOT {self.subexpression})"
# Eq() accepts 2 Literals and compares them to each other
# ex: 2 == 3 = False
# ex: Eq(Lit(2), Lit(3)) = False
@dataclass
class Eq():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} == {self.right_val})"
# NEq() accepts 2 Literals and compares them to each other
# ex: 2 != 3 = True
# ex: NEq(Lit(2), Lit(3)) = True
@dataclass
class NEq():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} != {self.right_val})"
# Lt() accepts 2 integers and compares them to each other
# ex: 2 < 3 = True
# ex: Lt(Lit(2), Lit(3)) = True
@dataclass
class Lt():
    left_val:ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} < {self.right_val})"
# LtE() accepts 2 integers and compares them to each other
# ex: 2 <= 3 = True
# ex: LtE(Lit(2), Lit(3)) = True
@dataclass
class LtE():
    left_val:ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} <= {self.right_val})"
# Gt() accepts 2 integers and compares them to each other
# ex: 2 > 3 = False
# ex: Gt(Lit(2), Lit(3)) = False
@dataclass
class Gt():
    left_val:ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} > {self.right_val})"
# GtE() accepts 2 integers and compares them to each other
# ex: 2 >= 3 = False
# ex: GtE(Lit(2), Lit(3)) = False
@dataclass
class GtE():
    left_val:ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} >= {self.right_val})"
# If() accepts 3 expressions for a condition, a primary branch and a secondary branch
@dataclass
class If():
    condition: ExpressionType
    then_sect: ExpressionType
    else_sect: ExpressionType
    def __str__(self) -> str:
        return f"(if {self.condition} \n\tthen {self.then_sect} \n\telse {self.else_sect})"
# Domain-specific Library functions and implementation
# Append merges 2 strings of characters and returns the value
@dataclass
class Append():
    left_val: ExpressionType
    right_val: ExpressionType
    def __str__(self) -> str:
        return f"({self.left_val} += {self.right_val})"
# Replace() takes an initial string and replaces the first instance of a given 
# string and replaces it with another given string
@dataclass
class Replace():
    initial_string: ExpressionType
    to_replace: ExpressionType
    replacement: ExpressionType
    def __str__(self) -> str:
        return f"(in {self.initial_string} replacing first {self.to_replace} with {self.replacement})"
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
@dataclass
class Letfun():
    name: str
    param: str
    bodyexpr: ExpressionType
    inexpr: ExpressionType
    def __str__(self) -> str:
        return f"letfun {self.name} ({self.param}) = {self.bodyexpr} in {self.inexpr} end"
@dataclass
class App():
    fun: ExpressionType
    arg: ExpressionType
    def __str__(self) -> str:
        return f"({self.fun} ({self.arg}))"
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
type blank = int | bool | str | Closure
@dataclass
class Closure():
    param:str
    body:ExpressionType
    env: Environment[blank]
def eval(e: ExpressionType) -> blank:
    return evalInEnv(blank_env, e)
def evalInEnv(env: Environment[blank], e: ExpressionType) -> blank:
    match e:
        # environment implementation for integer arithmetic
        case Add(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (bool(lv), int(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (bool(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), int(rv)):
                    return lv + rv
                case _:
                    raise evaluate_error("addition of non-integer values")
        case Sub(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (bool(lv), int(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (bool(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), int(rv)):
                    return lv - rv
                case _:
                    raise evaluate_error("subtraction of non-integer values")
        case Mul(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (bool(lv), int(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (bool(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), int(rv)):
                    return lv * rv
                case _:
                    raise evaluate_error("multiplication of non-integer values")
        case Div(left_val,right_val):
            match (evalInEnv(env,left_val), evalInEnv(env,right_val)):
                case (bool(lv), int(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (bool(lv), bool(rv)):
                    raise evaluate_error("addition of non-integer values")
                case (int(lv), int(rv)):
                    if rv == 0:
                        raise evaluate_error("division by zero")
                    return lv // rv
                case _:
                    raise evaluate_error("division of non-integer values")                
        case Neg(s):
            match evalInEnv(env,s):
                case bool(i):
                    raise evaluate_error("negation of non-integer value")
                case int(i):
                    return -i
                case _:
                    raise evaluate_error("negation of non-integer value")
        # environment implementation of boolean arithmetic
        case And(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            if not isinstance(left_eval, bool):
                raise evaluate_error("AND comparison of non-boolean values")
            if not left_eval:  # Short-circuit: If the left operand is False, return False directly
                return False
            right_eval = evalInEnv(env, right_val)
            if not isinstance(right_eval, bool):
                raise evaluate_error("AND comparison of non-boolean values")
            return right_eval
        case Or(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            if not isinstance(left_eval, bool):
                raise evaluate_error("OR comparison of non-boolean values")
            if left_eval:  # Short-circuit: If the left operand is True, return True directly
                return True
            right_eval = evalInEnv(env, right_val)
            if not isinstance(right_eval, bool):
                raise evaluate_error("OR comparison of non-boolean values")
            return right_eval
        case Not(subexpression):
            match (evalInEnv(env, subexpression)):
                case (bool(i)):
                    return not i
                case _:
                    raise evaluate_error("NOT transformation of a non-boolean value")
        case Eq(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                return False
            return left_eval == right_eval
        case NEq(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                raise evaluate_error("EQ comparison of different types")
            return left_eval != right_eval
        case Lt(left_val, right_val):  
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                raise evaluate_error("LT comparison of different types")
            if not isinstance(left_eval, int) or not isinstance(right_eval, int):
                raise evaluate_error("LT comparison of non-integer values")
            return left_eval < right_eval
        case LtE(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                raise evaluate_error("LTE comparison of different types")
            if not isinstance(left_eval, int) or not isinstance(right_eval, int):
                raise evaluate_error("LTE comparison of non-integer values")
            return left_eval <= right_eval
        case Gt(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                raise evaluate_error("GT comparison of different types")
            if not isinstance(left_eval, int) or not isinstance(right_eval, int):
                raise evaluate_error("GT comparison of non-integer values")
            return left_eval > right_eval
        case GtE(left_val, right_val):
            left_eval = evalInEnv(env, left_val)
            right_eval = evalInEnv(env, right_val)
            if type(left_eval) != type(right_eval):
                raise evaluate_error("GTE comparison of different types")
            if not isinstance(left_eval, int) or not isinstance(right_eval, int):
                raise evaluate_error("GTE comparison of non-integer values")
            return left_eval >= right_eval
        case If(condition, then_sect, else_sect):
            match (evalInEnv(env, condition)):
                case (bool(c)):
                    if c:
                        return evalInEnv(env, then_sect)
                    else:
                        return evalInEnv(env, else_sect)
                case _:
                    raise evaluate_error("IF condition of a non-boolean value")
        # environment implementation for domain-specific functions
        case Append(left_val, right_val):
            match (evalInEnv(env, left_val), evalInEnv(env, right_val)):
                case (str(lv), str(rv)):
                    return lv + rv
                case _:
                    raise evaluate_error("appending of non-string values")
        case Replace(initial_string, to_replace, replacement):
            match (evalInEnv(env, initial_string), evalInEnv(env, to_replace), evalInEnv(env, replacement)):
                case(str(istring), str(torep), str(repl)):
                    return istring.replace(torep, repl, 1)
                case _:
                    raise evaluate_error("REPLACE operation with non-string values")
        # environment implementation of let and binding
        case Lit(lit) :
            match lit:  # two-level matching keeps type-checker happy
                case int(i):
                    return i
                case bool(i):
                    return i
                case str(i):
                    return i
                case _:
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
        case Letfun(n,p,b,i):
            c = Closure(p,b,env)
            newEnv = extend_environment(n,c,env)
            c.env = newEnv
            return evalInEnv(newEnv,i)
        case App(f,a):
            fun = evalInEnv(env,f)
            arg = evalInEnv(env,a)
            match fun:
                case Closure(p,b,cenv):
                    newEnv = extend_environment(p,arg,cenv)
                    return evalInEnv(newEnv,b)
                case _:
                    raise evaluate_error("application of non-function entity")
def run(e: ExpressionType) -> None:
    print(f"running: {e}")
    try:
        match eval(e):
            case int(i):
                print(f"result: {i}")
            case bool(i):
                print(f"result: {i}")
            case str(i):
                print(f"result: {i}")
    except evaluate_error as err:
        print(err)

# Tests
'''
# Usage of Append()
a: ExpressionType = Append(Lit("foo"), Lit("bar"))
run(a)
b: ExpressionType = Append(Lit(123), Lit(456))
run(b)
c: ExpressionType = Append(Lit(True), Lit(False))
run(c)

# Usage of Replace()
d: ExpressionType = Replace(Lit("WAwarwala"), Lit("war"), Lit("iou"))
run(d)
e: ExpressionType = Replace(Lit(123), Lit(2), Lit(4))
run(e)
'''
'''
    The domain i chose to implement is the usage of strings.
    it is intended to be used for appending to strings (Append()) and 
    taking a string and replacing a given substring with another string (Replace())
'''
