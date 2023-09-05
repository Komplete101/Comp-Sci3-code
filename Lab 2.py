#Created an array of the 10 day highs
highttemperature = [95,97,99,99, 96,90,85,84,83,81]
#Obtained a specific index and printed it
day5 =highttemperature[4]
print("The day 5 forcast is: " + str(day5))
day7 =highttemperature[6]
print("The day 7 forcast is: " + str(day7))
#Sliced the orginal temperature list in the middle
print('The temperatures for the next five days are '+ str(highttemperature[:5]))
print('The temperatures for the last five days are '+ str( highttemperature[5:]))

"""Create a new variable with the 
11th days temperature, added it to 
the list and printed the list"""
day11 = 77
highttemperature.append(day11)
print('The 11 day highs temperature are '+ str(highttemperature))

#Removed the last element from the list
highttemperature.pop(0)
print("Here is the new 10 day forcast " + str(highttemperature))