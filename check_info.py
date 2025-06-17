import loadsave_tofile as ltf


def id_check(must_exist=True):
    while True:

        master_list = ltf.load_file("Product List.json").index
        print("Input the Product ID")
        product_id_input = input("Product ID: ").upper().strip()  # Product ID / Bar Code
        exist = product_id_input in master_list.values

        if not must_exist and exist:
            print(f"{product_id_input} has been registered")

        elif must_exist and not exist:
            print(f"{product_id_input} is not registered yet")

        else:
            return product_id_input

        print("\nDo you want to:")
        print(f"1. Re-input the product id?")
        print("2. Go back to the main menu?")
        while True:
            try:
                proceed_or_not = int(input("= "))
                if proceed_or_not == 1:
                    break  # to repeat checking product_id while loop
                elif proceed_or_not == 2:
                    print("Going back to main menu")
                    return None
                else:
                    print("Invalid input. Please choose a number between 1 or 2")
                    continue
            except ValueError:
                print("Invalid input. Please choose a number between 1 or 2")
                continue
