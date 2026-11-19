# compound interest using function
def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    ci = amount - p
    return ci, amount

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in Years: "))

ci, amount = compound_interest(p, r, t)

print("Compound Interest =", ci)
print("Total Amount =", amount)
