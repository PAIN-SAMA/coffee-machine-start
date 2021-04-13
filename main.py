from data import MENU
from data import resources


is_on = True
profit = 0


def is_resources_sufficient(order_ingredients):
  """ return True when order can be made, False if ingredients are insufficient """
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"sorry there is no enough {item}. ")
      return False
  return True


def process_coins():
  """ return the total calculated from coin inserted """
  print("please insert coins.")
  total = int(input("how manny quarters?  0.25$ ")) * 0.25
  # total += int(input("how manny dimes?  0.10$ ")) * 0.10
  # total += int(input("how manny nickels? 0.05$ ")) * 0.05
  # total += int(input("how manny pennies? 0.01$ ")) * 0.01
  return total


def is_trasaction_successful(money_received, drink_cost):
  """return True when payment accepted, or False if money insufficient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change")
    global profit
    profit += drink_cost
    return True
  else:
    print("sorry money is not enough.")
    return False


def make_coffee(drink_name, order_ingredients):
  """reduce ingredients from resources"""
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")


while is_on:
  choice = input("What would you like? (espresso, latte, capuuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"  Water: {resources['water']}ml")
    print(f"  Milk: {resources['milk']}ml")
    print(f"  Coffee: {resources['coffee']}gm")
    print(f"  monry: ${profit}")
  else:
    drink = MENU[choice]
    if is_resources_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_trasaction_successful(payment, drink["cost"]):
        make_coffee(choice, drink["ingredients"])