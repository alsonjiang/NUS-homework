#fun with digits

#3.1 Equal To
#ops = {+, -, *, %}
def equal_to(lhs: str, rhs: int, ops: str) -> set:

    def generate_expressions(prefix, digits):
        if not digits:
            if safe_eval(prefix) == rhs:
                correct_equations.add(prefix + '=' + str(rhs))
            return
        # No operator, just append the next digit
        generate_expressions(prefix + digits[0], digits[1:])
        # Try each operator
        for op in ops:
            generate_expressions(prefix + op + digits[0], digits[1:])

    def safe_eval(expr):
        # Replace '%' with '//' for modulo operation
        expr = expr.replace('%', '//')
        try:
            # Here we're using eval. This is typically safe since we're only evaluating
            # expressions that we've constructed ourselves with known good inputs.
            return eval(expr)
        except ZeroDivisionError:
            return None  # Ignore divide by zero errors

    correct_equations = set()
    generate_expressions(lhs[0], lhs[1:])
    return correct_equations

def product(s, n):
    if n == 0:
        return ['']  # Base case: single empty string for 0-length product
    if n == 1:
        return list(s)  # Base case: single characters for 1-length product
    
    # Get the product of s with n-1
    prev_product = product(s, n - 1)
    
    # Now, prepend each character of s to each item in the previous product
    result = []
    for char in s:
        for item in prev_product:
            result.append(char + item)
    
    return result

# Example usage:
#print(product('ab', 3))
#print(product('xyz', 2))
#['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
#['xx', 'xy', 'xz', 'yx', 'yy', 'yz', 'zx', 'zy', 'zz']


#print(equal_to('199', 100, '+'))
#print(equal_to('123456789',100,'+'))
