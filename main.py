import product_catalog as pc
import inventory as inv
import loadsave_tofile as ltf


def main_menu():
    print("\n-----------------------------")
    print("Available operation")
    print("-----------------------------")
    print("1. Product Catalog")
    print("2. Update Inventory")
    print("3. StockIn")
    print("4. Sold Item")
    print("5. TransactionHistory")
    print("6. ReportPrinter")
    print("7. Exit")
    print("-----------------------------")


def id_check(must_exist=True):
    master_list = ltf.load_catalog().index
    print("Input the Product ID")
    product_id_input = input("Product ID: ").capitalize().strip()  # Product ID / Bar Code
    exist = product_id_input in master_list.values

    if not must_exist and exist:
        print(f"{product_id_input} has been registered")

    elif must_exist and not exist:
        print(f"{product_id_input} is not registered yet")
    else:
        return product_id_input

    print("\nDo you want to:")
    print("1. Re-input the product id?")
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


while True:

    main_menu()
    user_input = input("\nSelect the number for the operation: ")

    match user_input:
        # 1. Product Catalog
        case "1":
            product_id = id_check(must_exist=False)
            if product_id is None:
                continue
            pc.add_product(product_id)
        # 2. Inventory
        case "2":
            product_id = id_check(must_exist=True)
            if product_id is None:
                continue
            inv.update_inv(product_id)
        # 3. StockIn
        case "3":
            pass
        # 4. Sold
        case "4":
            pass
        # 5. TransactionHistory
        case "5":
            pass
        # 6. ReportPrinter
        case "6":
            pass
        # Exit
        case "7":
            print("-----------------------------")
            print("Exit the Program...")
            break
        case _:
            print("Invalid input. Please choose a number between 1-7")
