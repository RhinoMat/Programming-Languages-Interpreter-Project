from project.interp import *
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