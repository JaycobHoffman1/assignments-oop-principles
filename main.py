from budget_category import BudgetCategory

food_category = BudgetCategory("Food", 500)

# Adding expenses

print("Adding expenses:\n")

food_category.add_expense(100)
food_category.add_expense(25)
food_category.add_expense(150)
food_category.add_expense(50)
food_category.add_expense(175)
food_category.display_category_summary()

# Example of trying to add a negative expense (raises ValueError)

print("\nExample of trying to add a negative expense (-10):")

food_category.add_expense(-10)

# Example of trying to pass a non-numeric value into the "add_expense()" function (raises ValueError)

print("\nExample of trying to pass a non-numeric value (\"fifty\") into the \"add_expense()\" function:")

food_category.add_expense("fifty")

# Changing category name:

print("\nChanging category name:")

food_category.set_category_name("Groceries")

print(f"New category name: {food_category.get_category_name()}")

# Changing allocated budget:

print("\nChanging allocated budget:")

food_category.set_allocated_budget(600)

print(f"New allocated budget: {food_category.get_allocated_budget()}")