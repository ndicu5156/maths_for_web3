
def gcd(m, a):
    while a != 0:
        m, a = a, m % a
    return m

def congruence(a,c,m):
    gcd_value=gcd(m ,a)
    if c % gcd_value !=0 :
        return f"error {gcd_value} does not divide {c} so no solutions"

    else:
        return f" {gcd_value} divides {c} so the equation has {gcd_value} solutions"

result=congruence(a,c,m)
print (result)

def gcd_extended(a, b):
    
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
def solve_congruence(a, c, m):
    
    
    gcd_value, x_coeff, _ = gcd_extended(a, m)
    
 
    if c % gcd_value != 0:
        return f"Error: gcd({m}, {a}) = {gcd_value} does not divide {c}, so no solution exists."
    
    a_simplified = a // gcd_value
    c_simplified = c // gcd_value
    m_simplified = m // gcd_value

    _, inverse_a, _ = gcd_extended(a_simplified, m_simplified)
    x0 = (inverse_a * c_simplified) % m_simplified
    solutions = []
    for k in range(gcd_value):
        solution = (x0 + k * m_simplified) % m
        solutions.append(solution)

    return f"The gcd({m}, {a}) = {gcd_value}, so there are {gcd_value} solutions: {solutions}"

result=solve_congruence(a,c,m)
print(result)
    
