from decimal import Decimal
from refrigerator import refrigerate

TWOPLACES = Decimal(10) ** -2
print 'Air conditioner started working'
cost = Decimal(refrigerate(30, 20, 360))
print 'The cost maintaining temperature at 20 degrees for 360 minutes was R$ ' + str(cost.quantize(TWOPLACES)) + ', with initial temperature of 30 degrees.'
