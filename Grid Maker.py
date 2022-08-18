import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))

print("Grid size entered: " + str(rows) + ' x ' + str(columns))

w = float(input("Enter the width of the lid: "))
h = float(input("Enter the height of the lid: "))

print("Lid size entered: " + str(w) + ' x ' + str(h))

startingx = int(input("Enter the starting x value: "))
endingx = int(input("Enter the ending x value: "))
startingy = int(input("Enter the starting y value: "))
endingy = int(input("Enter the ending y value: "))

list1 = list(range(startingx, endingx + 1))
list2 = list(range(startingy, endingy + 1))

coord = []

for x in list1:
    nl = []
    for y in list2:
        nl.append('(' + str(x) + ', ' + str(y) +')')
    coord.append((nl))

cord = np.array(coord)

num_cord = len(cord)

num_ent = rows * columns

R = endingx - startingx + 1
C = endingy - startingy + 1
        
x = cord.reshape(R, C)

itera = num_ent / num_cord
print(itera)
print(num_cord)
print(num_ent)
while itera > 0:
    fig, axes = plt.subplots(rows, columns, constrained_layout=True, sharex='row', sharey='col')
    plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
    for row in range(rows):
        for col in range(columns):
            axes[row, col].text(0.5, 0.5, 
                              str((row, col)),
                              color="black",
                              ha='center')
        itera = itera - 1 
    plt.show()
       