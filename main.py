import product_catalog as pc
import inventory as inv
import loadsave_tofile as ltf
import check_info as ci


# Important!!!!!
# This program main reference file is Product List.
# Once product list's file corrupt, the whole program will fail.
# Inventory and Sales file also refer to the Product List.
# Highest priority of maintaining the Product List file is a must.

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
    print("8. View products list")
    print("-----------------------------")


while True:

    main_menu()
    user_input = input("\nSelect the number for the operation: ")

    match user_input:
        # 1. Product Catalog
        case "1":
            # add password in the future
            product_id = ci.id_check(must_exist=False)
            if product_id is None:
                continue
            pc.add_product(product_id)
        # 2. Inventory
        case "2":
            inv.update_inv()
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
        case "8":
            ltf.show_list()

        case _:
            print("Invalid input. Please choose a number between 1-7")
