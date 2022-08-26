


# from tokenize import _Position
from turtle import position


row1 = ["🔒","🔒","🔒"]
row2 = ["🔒","🔒","🔒"]
row3 = ["🔒","🔒","🔒"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print(input("Where is you want to put the tresure ?"))#frist put row number and then coloum number

horizonal = (position[0]) 
vertical = (position[1])

map[vertical-1][horizonal-1] = "🔑"

print(f"{row1}\n{row2}\n{row3}")

