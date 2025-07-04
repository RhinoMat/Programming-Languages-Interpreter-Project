from interp import Add, Sub, Mul, Div, Neg, Let, Name, Lit, If, ExpressionType, And, Or, Lt, LtE, Gt, GtE, Not, NEq, Eq, run, Letfun, App, Append, Replace, Search, Exp, Assign, Seq, Show, Read
from lark import Lark, Token, ParseTree, Transformer
from lark.exceptions import VisitError
from pathlib import Path

# parser brings in the interpreter grammar from lark and uses a parser style
parser = Lark(Path('expr.lark').read_text(),start='expr',parser='earley',ambiguity='explicit')
class ParseError(Exception):
    pass
def parse(s: str) -> ParseTree:
    try:
        return parser.parse(s)
    except Exception as e:
        raise ParseError(e)

class AmbiguousParse(Exception):
    pass

# translates statements given in the expression from human language into functions to funnel the information
class ToExpr(Transformer[Token,ExpressionType]):
    def plus(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Add(args[0], args[1])
    def minus(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Sub(args[0], args[1])
    def times(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Mul(args[0], args[1])
    def divide(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Div(args[0], args[1])
    def expon(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Exp(args[0], args[1])
    def neg(self, args: tuple[ExpressionType]) -> ExpressionType:
        return Neg(args[0])
    def and_(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return And(args[0], args[1])
    def or_(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Or(args[0], args[1])
    def not_(self, args: tuple[ExpressionType]) -> ExpressionType:
        return Not(args[0])
    def eq(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Eq(args[0], args[1])
    def neq(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return NEq(args[0], args[1])
    def lt(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Lt(args[0], args[1])
    def lte(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return LtE(args[0], args[1])
    def gt(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Gt(args[0], args[1])
    def gte(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return GtE(args[0], args[1])
    def let(self, args: tuple[Token, ExpressionType, ExpressionType]) -> ExpressionType:
        return Let(args[0].value, args[1], args[2])
    def if_(self, args: tuple[ExpressionType, ExpressionType, ExpressionType]) -> ExpressionType:
        return If(args[0], args[1], args[2])
    def append(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Append(args[0], args[1])
    def replace(self, args: tuple[ExpressionType, ExpressionType, ExpressionType]) -> ExpressionType:
        return Replace(args[0], args[1], args[2])
    def search(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Search(args[0], args[1])
    def id(self, args:tuple[Token]) -> ExpressionType:
        return Name(args[0].value)
    def int_literal(self, args: tuple[Token]) -> ExpressionType:
        return Lit(int(args[0].value))
    #def true_literal(self, _) -> ExpressionType:
    #    return Lit(True)
    #def false_literal(self, _) -> ExpressionType:
    #    return Lit(False)
    def string_literal(self, args: tuple[Token]) -> ExpressionType:
        return Lit(args[0].value[1:-1])  # Remove the quotes
    def letfun(self,args:tuple[Token,Token,ExpressionType,ExpressionType]) -> ExpressionType:
        return Letfun(args[0].value,args[1].value,args[2],args[3])
    def app(self,args:tuple[ExpressionType,ExpressionType]) -> ExpressionType:
        return App(Name(args[0]),args[1])
    def bool_literal(self, args: tuple[Token]) -> ExpressionType:
        return Lit(args[0].value == "true")
    def assign(self, args: tuple[Token, ExpressionType]) -> ExpressionType:
        return Assign(args[0].value, args[1])
    def seq(self, args: tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        if isinstance(args[0], Seq):
            return Seq(args[0].first, Seq(args[0].second, args[1]))
        return Seq(args[0], args[1])
    def show(self, args: tuple[ExpressionType]) -> ExpressionType:
        return Show(args[0])
    def read(self, _) -> ExpressionType:
        return Read()
    def _ambig(self,_) -> ExpressionType:
        print("Ambiguous parse detected:", _)
        raise AmbiguousParse()
def genAST(t:ParseTree) -> ExpressionType:
    '''Applies the transformer to convert a parse tree into an AST'''
    # boilerplate to catch potential ambiguity error raised by transformer
    try:
        return ToExpr().transform(t)               
    except VisitError as e:
        if isinstance(e.orig_exc,AmbiguousParse):
            raise AmbiguousParse()
        else:
            raise e

def driver():
    while True:
        try:
            s = input('expr: ')
            t = parse(s)
            print("raw:", t)    
            print("pretty:")
            print(t.pretty())
            ast = genAST(t)
            print("raw AST:", repr(ast))  # use repr() to avoid str() pretty-printing
            run(ast)                      # pretty-prints and executes the AST
        except AmbiguousParse:
            print("ambiguous parse")                
        except ParseError as e:
            print("parse error:")
            print(e)
        except EOFError:
            break

def parse_and_run(s:str):
    try:
        t = parse(s)
        print("raw:", t)    
        print("pretty:")
        print(t.pretty())
        ast = genAST(t)
        print("raw AST:", repr(ast))  # use repr() to avoid str() pretty-printing
        run(ast)                      # pretty-prints and executes the AST
    except AmbiguousParse:
        print("ambiguous parse")                
    except ParseError as e:
        print("parse error:")
        print(e)
def just_parse(s:str):
    t = parse(s)
    return genAST(t)
#if __name__  == "__main__":
#    driver()
