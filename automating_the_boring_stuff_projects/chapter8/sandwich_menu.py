# this program provides users to make a sandwich with the given options in the menu
import pyinputplus as pyip

# ask questions to user
bread = pyip.inputMenu(prompt="Select bread type (wheat, white, sourdough):\n", choices=["wheat", "white", "sourdough"])
protein = pyip.inputMenu(prompt="Select protein type (chicken, turkey, ham or tofu):\n", choices=["chicken", "turkey", "ham", "tofu"])
is_cheese = pyip.inputYesNo(prompt="Do you want to add cheese (yes or no)? ")
if is_cheese == "yes":
    cheese = pyip.inputMenu(prompt="Select cheese type (cheddar, Swiss, mozzarella):\n", choices=["cheddar", "Swiss", "mozzarella"])
sandwich_num = pyip.inputNum(prompt="How many sandwiches do you want? ", min=1)

# display which options user have selected
print(bread)
print(protein)
if is_cheese == "yes":
    print(cheese)
print(sandwich_num)