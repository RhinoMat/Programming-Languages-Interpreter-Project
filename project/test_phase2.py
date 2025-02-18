import unittest
from parse_run import parse, genAST, run, AmbiguousParse, ParseError

class TestInterpreter(unittest.TestCase):
    def test_addition(self):
        expr = "1 + 2"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(1 + 2)")
        run(ast)

    def test_subtraction(self):
        expr = "5 - 3"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(5 - 3)")
        run(ast)

    def test_multiplication(self):
        expr = "4 * 2"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(4 * 2)")
        run(ast)

    def test_division(self):
        expr = "8 / 4"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(8 / 4)")
        run(ast)

    def test_negation(self):
        expr = "-5"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(- 5)")
        run(ast)

    def test_boolean_and(self):
        expr = "true && false"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), str(expr))
        run(ast)

    def test_boolean_or(self):
        expr = "true || false"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(true || false)")
        run(ast)

    def test_boolean_not(self):
        expr = "!true"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(NOT true)")
        run(ast)

    def test_let(self):
        expr = "let x = 5 in x + 3 end"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(let x = 5 in (x + 3))")
        run(ast)

    def test_if(self):
        expr = "if true then 1 else 0"
        t = parse(expr)
        ast = genAST(t)
        self.assertEqual(str(ast), "(if true \n\tthen 1 \n\telse 0)")
        run(ast)

    def test_ambiguous_expression(self):
        expr = "1 + 2 * 3"
        with self.assertRaises(AmbiguousParse):
            t = parse(expr)
            genAST(t)

    def test_parse_error(self):
        expr = "let x = 5 in x + end"
        with self.assertRaises(ParseError):
            parse(expr)

if __name__ == '__main__':
    unittest.main()