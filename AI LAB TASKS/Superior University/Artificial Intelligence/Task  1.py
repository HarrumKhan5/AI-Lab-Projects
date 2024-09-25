class FriendlyCalculator:
    def __init__(self):
        print("Hello! Welcome to your friendly calculator.")
        print("Perform addition, subtraction, multiplication, and division using BODMAS rule.")
        print("Enter your expressions, and lemme do the calculations for you!")
        print("Remember to use parentheses for complex expressions (e.g., (2 + 3) * 4 / 2).")
        print("To stop, just type 'exit'.")
    def calc_expression(self, expression):
        try:
            result = eval(expression)
            return (f"The result is: {result}")
        except ZeroDivisionError:
            return ("Oh-no! I guess you're trying to divide by zero. That’s not allowed!")
        except Exception as e:
            return (f"Oops! Something went wrong: {e}. Please check your expression and try again.")

    def operate(self):
        while True:
            expression = input("Enter your expression (or type 'exit' to quit): ")
            if expression.lower() == 'exit':
                print("Goodbye! It was fun calculating with you. See you next time!")
                break
            result = self.calc_expression(expression)
            print(result)
calc = FriendlyCalculator()
calc.operate()
