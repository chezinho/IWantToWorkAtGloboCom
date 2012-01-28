from decimal import Decimal
from refrigerator import refrigerate

TWOPLACES = Decimal(10) ** -2
print 'Air conditioner started working'
result = refrigerate(30, 20, 360)
final_temperature = result[0]
cost = Decimal(result[1])
print 'The cost maintaining temperature at 20 degrees for 360 minutes was R$ ' + str(cost.quantize(TWOPLACES)) + ', with initial temperature of 30 degrees.'
print 'The final temperature was ' + str(final_temperature) + ' degrees.'
