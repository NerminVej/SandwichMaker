import pyinputplus as pyip
# This program asks about the users sandwich preferences.

"""
We start with a print message that tells the user what this program does
We then create variables for each input value
bread, protein, cheese, cheeseType, mayo, mustard, lettuce, tomato, howMany
Afterwards we do the different inputs

Give each ingredient their price
store them in a dictionary called ingredients
ingredients["white"] = 0.34 for example
take the ingredient the user took and put them into a list called totalIngredients
for loop through all items in the list and use the ingredient to get the value fromm the ingredients dictionary
make a sum variable which stores all the prices
output the sum variable with a string
"""
# Price list of all the ingredients
ingredients = {"wheat":0.34, "white":0.20, "sourdough":0.46, "chicken":1.20, "turkey":1.50, "ham":1.10, "tofu":1.30,
               "cheddar":1.00,"swiss":1.80,"mozzarella":1.50,"mayo":0.15,"mustard":0.14,"lettuce":0.18,"tomato":0.20}
# Empty list that the user will fill throughout the programs use
userSandwich = []
sum = 0

print("Welcome and have fun creating your own burger!")


bread = pyip.inputMenu(["wheat", "white","sourdough"], "Select your bread type:\n")
protein = pyip.inputMenu(["chicken", "turkey","ham","tofu"], "Select your protein type:\n")
cheese = pyip.inputYesNo("Do you want Cheese? (Yes or No)")
cheeseType = pyip.inputMenu(["cheddar", "swiss","mozzarella"], "Select your cheese type:\n")
mayo = pyip.inputYesNo("Do you want mayo?")
mustard= pyip.inputYesNo("Do you want mustard?")
lettuce = pyip.inputYesNo("Do you want lettuce?")
tomato = pyip.inputYesNo("Do you want tomato?")

# We put every value inside a new list
userSandwich.extend([bread,protein,cheeseType,mayo,mustard,lettuce,tomato])

for entry in userSandwich:
    if entry in ingredients:
        sum += ingredients[entry]


sandwichesCount = pyip.inputInt("How many sandwiches do you want?" , min=1)
sum = sum * sandwichesCount

print("The total cost of your purchase is: " + str(sum) + "€")