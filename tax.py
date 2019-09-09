'''\
tax.py
Take some input, apply some rules, computes a simplified income tax.
'''

#input name
name = input('What is your name? ')

# input taxable income
strTaxInc = (input('What is your taxable income? '))
fltTaxInc = float(strTaxInc)

# input number of dependents
strNumDep = input('How many dependents do you have? ')
fltNumDep = float(strNumDep)


DEDUCTION = 100000
DEP_AMT = 3000
#fltNum = strTaxInc
fltAGI = fltTaxInc - DEDUCTION - fltNum * DEP_AMT

# compute 10% tax
fltTax10 = fltAGI * 0.1
fltTax15 = fltAGI * 0.15
fltTax20 = fltAGI * 0.2

# output
print('Tax for ', name,'at 10% = ', fltTax10)
print('Tax at 15% = ', fltTax15)
print('Tax at 20% = ', fltTax20)

