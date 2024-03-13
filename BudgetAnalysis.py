import matplotlib.pyplot as plt

# Check your budget
class InputData:
    def __init__(self):
        self.income = 0
        self.expenses = {"loan": 0, "rent and utilities": 0, "food": 0, "clothing": 0, "entertainment": 0, "education": 0,
                         "health": 0, "other expenses": 0}
        self.budget = []

    def input_income_expenses(self):
        while True:
            try:
                self.income = float(input("Enter your monthly income: "))
                while self.income < 0:
                    self.income = float(input("Income must be greater than 0! Enter your monthly income: "))
                break
            except ValueError:
                print("Income must be a number greater than 0! Please enter the correct data")

        while True:
            try:
                loan = float(input("Enter your monthly loan expenses: "))
                if loan < 0:
                    loan = float(input("Expenses must be greater than 0! Enter your monthly loan expenses: "))

                rent = float(input("Enter your monthly rent and utilities expenses: "))
                if rent < 0:
                    rent = float(input("Expenses must be greater than 0! Enter your monthly rent and utilities expenses: "))

                food = float(input("Enter your monthly food expenses: "))
                if food < 0:
                    food = float(input("Expenses must be greater than 0! Enter your monthly food expenses: "))

                clothing = float(input("Enter your monthly clothing expenses: "))
                if clothing < 0:
                    clothing = float(input("Expenses must be greater than 0! Enter your monthly clothing expenses: "))

                entertainment = float(input("Enter your monthly entertainment expenses (outings to restaurants, cinemas, etc.): "))
                if entertainment < 0:
                    entertainment = float(input("Expenses must be greater than 0! Enter your monthly entertainment expenses (outings to restaurants, cinemas, etc.): "))

                education = float(input("Enter your monthly education expenses: "))
                if education < 0:
                    education = float(input("Expenses must be greater than 0! Enter your monthly education expenses: "))

                health = float(input("Enter your monthly health expenses: "))
                if health < 0:
                    health = float(input("Expenses must be greater than 0! Enter your monthly health expenses: "))

                other = float(input("Enter your monthly expenses that have not been previously included: "))
                if other < 0:
                    other = float(input("Expenses must be greater than 0! Enter your monthly expenses that have not been previously included: "))

                self.expenses = {"loan": loan, "rent and utilities": rent, "food": food, "clothing": clothing,
                                 "entertainment": entertainment, "education": education, "health": health, "other expenses": other}
                break

            except ValueError:
                print("Expense must be a number greater than 0! Please enter the correct data")

        budget = Budget(self.income, self.expenses)
        self.budget.append(budget)

    def analyze_budget(self):
        for budget in self.budget:
            income = budget.get_income()
            print("Your monthly income is: " + str(income))
            expenses = budget.get_total_expenses()
            print("Your monthly expenses are: " + str(expenses))
            balance = budget.get_balance()
            if (balance < 0):
                print("This month you spent more than you earned :( Loss: " + str(-balance))
            else:
                print("This month you have a surplus of: " + str(balance))

            print("Here is the structure of your expenses: ")
            budget.print_expenses()

        charts = Charts()
        charts.expenses_chart(budget.get_expenses())
        charts.comparison_chart(budget.get_income(), budget.get_total_expenses())


class Budget:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses
        self.balance = self.income - sum(self.expenses.values())

    def get_income(self):
        return self.income

    def set_income(self, income):
        self.income = income
        self.balance = self.income - sum(self.expenses.values())

    def get_expenses(self):
        return self.expenses

    def get_total_expenses(self):
        return sum(self.expenses.values())

    def set_expenses(self, expenses):
        self.expenses = expenses
        self.balance = self.income - sum(self.expenses.values())

    def get_balance(self):
        return self.balance

    def print_expenses(self):
        for key, value in self.expenses.items():
            print(key, ":", value)


class Charts:
    def expenses_chart(self, expenses):
        plt.pie(expenses.values(), labels=expenses.keys())
        plt.title("Expenses Analysis")
        plt.show()

    def comparison_chart(self, income, total_expenses):
        data = [income, total_expenses]
        labels = ["Income", "Expenses"]
        plt.bar(labels, data)
        plt.show()


january = InputData()
january.input_income_expenses()
january.analyze_budget()
