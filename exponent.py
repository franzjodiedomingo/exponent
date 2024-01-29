# Calculates base raised to the power of exp
# Loop structure

def exponent(base, exp):
    result = 1
    for _ in range(exp): 
        result *= base
    return result

base = 2
exp = 5
result = exponent(base, exp)
print(f"{base}^{exp} = {result}")