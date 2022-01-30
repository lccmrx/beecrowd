import math
import re

n_input = int(input())

eqs = []
for i in range(n_input):
    eq = input().replace(" ", "")
    idxs = [match.span() for match in re.finditer(r'[-+*/]', eq)]
    eqs.append((eq, eq[idxs[1][0]], idxs[1][0], eq[:idxs[1][0]].split("/"), eq[idxs[1][0]+1::].split("/")))
    
op_map = {
    "+": lambda n1, d1, n2, d2 : f"{((n1 * d2) + (n2 * d1))}/{d1 * d2}",
    "-": lambda n1, d1, n2, d2 : f"{((n1 * d2) - (n2 * d1))}/{d1 * d2}",
    "*": lambda n1, d1, n2, d2 : f"{(n1 * n2)}/{d1 * d2}",
    "/": lambda n1, d1, n2, d2 : f"{(n1 * d2)}/{n2 * d1}",
}

for eq in eqs:
    op = eq[1]
    n1, d1 = int(eq[3][0]), int(eq[3][1])
    n2, d2 = int(eq[4][0]), int(eq[4][1])
    
    eq = op_map[op](n1, d1, n2, d2)
    
    simplified_eq = eq.split("/")
    n3, d3 = int(simplified_eq[0]), int(simplified_eq[1])
    mdc = math.gcd(n3, d3)
    simplified_eq = f"{int(n3/mdc)}/{int(d3/mdc)}"
    
    print(f"{eq} = {simplified_eq}")
