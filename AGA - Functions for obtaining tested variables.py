#Functions for obtaining tested variables
#Version 1.0
#Author: Alejandro Garcia Alonso

def obtainValueLoop(chain,converter):
     """
     Continuously prompts the user to enter a value until it can be successfully converted
     using the specified converter function.

     Args:
          chain (str): The prompt message shown to the user.
          converter (function): A function that attempts to convert the user input 
                                   (e.g., int, float, str, or a custom converter).

     Returns:
          Any: The successfully converted value, whose type depends on the converter used.

     Exceptions:
          - Prints an error message and retries if a ValueError occurs (e.g., invalid format).
          - Catches and prints any other unexpected exceptions.

     Example:
          value = obtainValueLoop("Enter an integer:", int)
          price = obtainValueLoop("Enter the price:", float)
     """
     while True:
        try:
            value = converter(input(chain + "\n"))
            break
        except ValueError:
            print("Incorrect Character. Try again")
        except Exception as e:
            print(f"Inesperated error: {e}") 
     return value         

def obtainInt(chain):
    return obtainValueLoop(chain,int)

def obtainFloat(chain):
    return obtainValueLoop(chain,float)

def obtainString(chain):
    return obtainValueLoop(chain,str)
