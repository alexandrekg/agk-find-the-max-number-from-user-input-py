
def main():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    result = max([first_number, second_number, third_number])
    print(f"The largest of the three numbers is: {result}")


if __name__ == "__main__":
    main()