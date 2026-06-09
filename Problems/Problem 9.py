# Special Pythagorean Triplet
# Answer:31875000 - a=200, b=375, c=425

def brute_force():
    # Since a < b < c, 'a' can never be more than 1/3 of 1000
    for a in range(1, 1000 // 3):
        for b in range(a + 1, 1000 // 2):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                product = a * b * c
                return f"a={a}, b={b}, c={c} | Product={product}"


def factorization():
    target_sum = 1000
    constant = (target_sum ** 2) // 2  # 500,000

    for a in range(1, target_sum // 3):
        if constant % (target_sum - a) == 0:
            b = target_sum - (constant // (target_sum - a))
            c = target_sum - a - b

            if a < b:
                return f"a={a}, b={b}, c={c} | Product={a * b * c}"


print(brute_force())