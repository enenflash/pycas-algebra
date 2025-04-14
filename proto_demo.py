from src import *
from prototype import *

# MATRICES
m1 = Matrix([[10, 7], [8, 1], [6, 9]])
m2 = Matrix([[7, 5], [3, 10]])
print(f"m1 = {m1}, m2 = {m2}")
print(f"m1 * m2 = {m1*m2}")
m3 = Matrix([[Term(1, {'x': 1}), Term(2, {'x': 2})], [Term(-1, {'x': 1}), Term(4, {'x': 1})]])
m4 = Matrix([[Term(-3, {'x': 1}), Term(1, {'x': 2})], [Term(3, {'x': 1}), Term(-2, {'x': 2})]])
print(f"m3 = {m3}, m4 = {m4}")
print(f"m3 * m4 = {m3*m4}")

# EQUATIONS
eq = Equation(3, Term(2, {'x': 1}))
print(f"solve({eq}) => x={eq.solve('x')}")
eq = Equation(0, (Term(1, {'x': 1})-Rational(1, 2))*(Term(1, {'x': 1})+Rational(2, 3)))
print(f"solve({eq}) => x={eq.solve('x')}")
eq = Equation(0, (Term(1, {'x': 1})*(Term(2, {'x': 1})-3)).expand())
print(f"solve({eq}) => x={eq.solve('x')}")
eq = Equation(0, (2*(Term(1, {'x': 1})+1)*(Term(1, {'x': 1})-6)*(Term(1, {'x': 1})+5)).expand())
print(f"solve({eq}) => x={eq.solve('x')}")
eq = Equation(0, ((Term(4, {'x': 1})+1)*(Term(3, {'x': 1})-2)*(Term(1, {'x': 1})+7)*(Term(8, {'x': 1})-3)).expand())
print(f"solve({eq}) => x={eq.solve('x')}")
eq = Equation(0, (Term(3, {'x': 1})-2)*(Term(7, {'x': 1})+1)**3*(Term(4, {'x': 1})-Rational(1, 2))*(Term(7, {'x': 1})-4)*(Term(3, {'x': 1})+4)**2)
print(f"solve({eq}) => x={eq.solve('x')}")

# irrational solutions (causes errors)
# exp = ((Term(1, {'x': 1})-Power(2, Rational(1, 2)))*(Term(1, {'x': 1})-2)).expand()
# print(exp)

# eq = Equation(0, exp)
# print(f"solve({eq}) => x={eq.solve('x')}")