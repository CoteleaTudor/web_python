from os import system
system ("cls")
from tax import calculateTax

salary    = float(input("introducetei suma salariului:  "))
interest  = float(input("introducetei procentajul:  "))
tax       = calculateTax(salary, interest, "salariu")
print(tax)

print()