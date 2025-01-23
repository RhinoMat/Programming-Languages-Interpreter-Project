# Interpreter that does boolean operations and normal arithmetic
# Module imports for processing
from dataclasses import dataclass
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
def eval(e: ExpressionType) -> int:
    return evalInEnv(blank_env, e)
def evalInEnv(env: Environment[int], e: ExpressionType) -> int:
    match e:
        case Add(left_val, right_val):
            return evalInEnv(env, left_val) + evalInEnv(env, right_val)
        case Sub(left_val,right_val):
            return evalInEnv(env,left_val) - evalInEnv(env,right_val)
        case Mul(left_val,right_val):
            leftv = evalInEnv(env,left_val)
            rightv = evalInEnv(env,right_val)
            return leftv * rightv
        case Div(left_val,right_val):
            leftv = evalInEnv(env,left_val)
            rightv = evalInEnv(env,right_val)
            if rightv == 0:
                raise evaluate_error("division by zero")
            return leftv // rightv
        case Neg(sub):
            return - (evalInEnv(env,sub))
        case Lit(int_val):
            return int_val
        case Name(name_val):
            val = lookup_environment(name_val, env)
            if val is None:
                raise evaluate_error(f"unbound name {name_val}")
            return val
        case Let(name,def_expr,body):
            val = evalInEnv(env, def_expr)
            newEnv = extend_environment(name, val, env)
            return evalInEnv(newEnv, body)
def run(e: ExpressionType) -> None:
    print(f"running: {e}")
    try:
        i = eval(e)
        print(f"result: {i}")
    except evaluate_error as err:
        print(err)

# testing area
a : ExpressionType = Let('x', Add(Lit(1), Lit(2)), 
                    Sub(Name('x'), Lit(3)))
print(a)

b : ExpressionType = Let('x', Lit(1), 
                    Let('x', Lit(2), 
                             Mul(Name('x'), Lit(3))))
print(b)  

c : ExpressionType = Add(Let('x', Lit(1), 
                        Sub(Name('x'), Lit(2))),
               Mul(Name('x'), Lit(3)))
print(c)

d : ExpressionType = Add(Lit(1), Div(Lit(2), Lit(0)))
print(d)

run(a)
run(b)
run(c)
run(d)
