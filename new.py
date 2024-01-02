try:
    user_input = input("Enter something: ")
    print("You entered:", user_input)
except EOFError:
    print("An EOFError occurred.")