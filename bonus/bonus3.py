#understanding for loops
meals = ['ugali','eggs','salad']

for meal in meals:
    #under the hood during the first iteration meal = ugali, thenf we can do ugali.capitalize, then in the second iteration meal = eggs
    print(meal.capitalize())

print("Bye")
#lists and strings are treated as sewuence and you can iterate over them
for character in "meals":
    #under the hood during the first iteration character = m, then we can do m.capitalize, then in the second iteration character = e
    print(character.capitalize())

#while loops execute as long as the condition is true,for loops execute till the end of the iteravles