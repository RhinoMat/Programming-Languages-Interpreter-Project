from project.interp import *
# testing area
# integer arithmetic
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

# boolean arithmetic
e : ExpressionType = Not(Lit(True))
print(e)

f : ExpressionType = Eq(Lit(True), Lit(False))
print(f)

g : ExpressionType = Lt(Lit(1), Lit(2))
print(g)

h : ExpressionType = If(Lit(True), Lit(1), Lit(2))
print(h)

i : ExpressionType = If(Lit(False), Lit(1), Lit(2))
print(i)

run(a)
run(b)
run(c)
run(d)
run(e)
run(f)
run(g)
run(h)
run(i)