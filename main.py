from logic import CalculatorLogic
from ui import CalculatorUI


def main():
    """
    Main entry point for the desktop calculator application.
    """
    # Initialize logic
    logic = CalculatorLogic()
    
    # Initialize UI and pass the logic evaluation callback
    # We use logic.evaluate directly
    app = CalculatorUI(logic.evaluate)
    
    # Run the application
    app.mainloop()


if __name__ == "__main__":
    main()
