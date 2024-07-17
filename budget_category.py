# Task 1: Define Budget Category Class

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    def check_if_positive(self, user_input, input_type):
        try:
            int(user_input)
        except ValueError:
            print(f"ERROR: {input_type} must be a numeric value.")

            return False
        
        try:
            if user_input < 0:
                raise ValueError(f"ERROR: {input_type} must be positive.")
        except ValueError as v:
            print(v)

            return False
        
        return True

    # Task 2: Implement Getters and Setters

    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    def set_allocated_budget(self, new_allocated_budget):
        if not self.check_if_positive(new_allocated_budget, "Budget"):
            return
        
        self.__allocated_budget = new_allocated_budget

    # Task 3: Add Budget Functionality

    amounts = []

    def add_expense(self, amount):
        if not self.check_if_positive(amount, "Amount"):
            return

        self.amounts.append(amount)

    def display_category_summary(self):
        print(f"{self.get_category_name()}:")

        for amount in self.amounts:
            print(amount)