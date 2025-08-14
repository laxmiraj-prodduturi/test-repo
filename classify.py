def classify():
    int_list = []
    float_list = []

    print("Enter numbers one by one (type 'done' to finish):")

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == 'done':
            break

        try:
            num = float(user_input)
            if num.is_integer():
                int_list.append(int(num))
            else:
                float_list.append(num)
        except ValueError:
            print("Invalid input, please enter a valid number.")

    print("Integers:", int_list)
    print("Floats:", float_list)
