# Operators and Order of Precedence - PEMDAS
print('Operators and Order of Precedence - PEMDAS')
print('()   **   *   /   //   %   +   -', end='\n'*2)
print('x = 2**(5-1)/4+12/6')
x = 2**(5-1)/4+12/6
print(x, end='\n'*2)

print(5 / 2, 'Normal Division', sep='\t')
print(5 // 2, 'Floor Division, Fraction is Cut-off', sep='\t')
print(5 % 2, 'Modulus, or Remainder after Division', sep='\t')
print(5 != 2, 'Not Equal To', sep='\t')

# Variable Conversions
print('Variable Conversions', end='\n'*2)

print(
    'number values',
    float(54)+1,
    int(754.7),
    int(-2.19),
    int(-2.99),
    int('754'),
    # int('754.777')+1     #error b/c its the value would be float and not integer
    float('754.777')+1,)

print(
    'string values',
    str(754.777),
    str(754/2),
    str(int(754/2)))

# Variable Types
print('Variable Types', end='\n'*2)

print('Data Values and Data Types')
print(
    type(None),
    type(True),
    type(-754),
    type(754.777),
    type('754'),
    sep='\n')

# Scientific Notation and .format
print('Scientific Notation and .format', end='\n'*2)

sf_val_1 = '{:e}'.format(0.0000001234)     # {:e} represents a float value
print("sf_val_1 = ", sf_val_1)

sf_val_2 = '{:.1e}'.format(12000000)
print("sf_val_2 = ", sf_val_2)

val_3 = 12340000
sf_val_3 = '{:e}'.format(val_3)
print("sf_val_3 = ", sf_val_3)
print('Float value of sf_val_3 = ', float('{:f}'.format(float(sf_val_3))))

print(round(14_847.104849))
print(round(14_847.104849, 3), 'round to 3 decimal places')

# Commas alter numeric values, but _ does not
print("Commas alter numeric values, but '_' does not", end='\n'*2)


# def venue_profit(n_attendees, x=2500):
def venue_profit(n_attendees):
    """Return the profit the venue generates from the number
    of attendees. The minimum number of attendees is 2,500
    venue_profit(3,000,2,500)
    45,000
    """
    return n_attendees*15


# print(venue_profit(12,500), "Incorrect value because a ',' was used in the number '12,500'", sep='\t')
print(venue_profit(12500), "Correct value b/c numbers cannot have commas '12500'", sep='\t')
print(venue_profit(12_500), "Correct value b/c numbers can use '_' '125_00' for readability", sep='\t')
