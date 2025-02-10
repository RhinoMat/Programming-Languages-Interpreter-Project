from interp import Add, Sub, Mul, Div, Neg, Let, Name, Lit, If, ExpressionType
from lark import Lark, Token, ParseTree, Transformer
from lark.exceptions import VisitError
from pathlib import Path

parser = Lark(Path('expr.lark').read_text(),start='expr',ambiguity='explicit')

class ParseError(Exception):
    pass
def parse(s: str) -> ParseTree:
    try:
        return parser.parse(s)
    except Exception as e:
        raise ParseError(e)

class AmbiguousParse(Exception):
    pass

class ToExpr(Transformer[Token,ExpressionType]):
    def plus(self, args:tuple[ExpressionType, ExpressionType]) -> ExpressionType:
        return Add(args[0], args[1])
    def _ambig(self,_) -> ExpressionType:
        raise AmbiguousParse()