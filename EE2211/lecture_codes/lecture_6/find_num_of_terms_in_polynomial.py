from math import comb

def number_of_polynomial_terms(n, d):
    # Calculate the sum of combinations from degree 0 to d
    total_terms = sum(comb(n + r - 1, r) for r in range(d + 1))
    return total_terms

#edit as necessary
n_features = 2
degree = 2
print(f"Number of polynomial terms for {n_features} features and degree {degree}:",
      number_of_polynomial_terms(n_features, degree))