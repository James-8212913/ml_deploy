from src import add as ad
from src import sub as sb
import main

from src import add

print("This take two numbers, add them then find the difference between them")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result_1 = ad.add(x,y)
print("The sum of the two figures is: ",result_1)
result_2 = sb.sub(x,y)
print("The difference between the two figures is: ", result_2)
