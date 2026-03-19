import math


class CalculatorLogic:
    """
    Handles the mathematical evaluation of calculations.
    """

    def evaluate(self, expression: str) -> str:
        """
        Evaluates a mathematical expression string and returns the result.
        Returns "Error" if the expression is invalid or encounters a zero division.
        """
        if not expression:
            return ""

        try:
            # Replace common symbols or formatting if needed
            # For simplicity, we use eval with restricted globals
            # We only allow basic math operators and math functions if needed
            # But the prompt specifies standard arithmetic operations.
            
            # Clean expression: remove any potential malicious input
            # Only allow digits, decimals, and basic operators: + - * / ( )
            allowed_chars = set("0123456789.+-*/() ")
            if not all(char in allowed_chars for char in expression):
                return "Error"

            # Check for consecutive operators (e.g., ++, +*, /+, etc.)
            # We allow - after an operator for negative numbers? 
            # For this simple requirement, we'll forbid all consecutive ones.
            operators = "+-*/"
            for i in range(len(expression) - 1):
                if expression[i] in operators and expression[i+1] in operators:
                    return "Error"

            # Use eval with no globals and only math functions if needed
            # For this simple calculator, we only need basic arithmetic.
            result = eval(expression, {"__builtins__": None}, {})
            
            # Formating result: convert float to int if its a whole number
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            return str(result)
        except ZeroDivisionError:
            return "Error"
        except (SyntaxError, TypeError, ValueError):
            return "Error"
        except Exception:
            return "Error"


if __name__ == "__main__":
    # Quick sanity check
    logic = CalculatorLogic()
    print(logic.evaluate("2+2"))       # Expected: 4
    print(logic.evaluate("10/2.5"))   # Expected: 4
    print(logic.evaluate("1/0"))       # Expected: Error
    print(logic.evaluate("invalid"))    # Expected: Error
