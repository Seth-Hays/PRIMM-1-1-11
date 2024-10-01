"""
PRIMM: 1+1 = 11
Description of program here
Seth - September 2024
"""

def main():
    # Delcaring variables and asking for input
    num1: float = float(input("Enter a number: "))
    num2: float = float(input("Enter another number: "))
    total: float = num1 + num2

    # Printing what you input
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} // {num2} = {num1//num2}")

if __name__ == "__main__":
  main()
