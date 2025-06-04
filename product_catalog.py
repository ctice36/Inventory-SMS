import pandas as pd
import loadsave_tofile as cf
import datetime as dt


def get_date():
    return dt.datetime.today()


# Return the new df of a new product
def add_product(prod_id):
    prod_name = input(f"Product Name: ").title().strip()
    prod_category = input(f"Product Categories: ").capitalize().strip()
    prod_price = round(float(input(f"Product Price (per unit): RM")), 2)
    supplier_name = input(f"Supplier Name: ").title().strip()
    supplier_id = input(f"Supplier ID: ").capitalize().strip()

    print(f"Please input the expiry code")
    print(f"1. Non-expire prod")
    print(f"2. Within 1 year.")
    print(f"3. Within 1 month")

    while True:
        try:
            expiry_flag = int(input(f"Expiry code: "))
            if not 0 < expiry_flag < 4:
                print("Input only 1, 2 or 3")
            else:
                break
        except ValueError:
            print("Input only 1, 2 or 3")
            continue

    today = get_date().strftime("%Y-%m-%d")
    other_item = None

    new_product = pd.DataFrame({"Product Name": [prod_name],
                                "Product Categories": [prod_category],
                                "Product Price": [prod_price],
                                "Supplier Name": [supplier_name],
                                "Supplier ID": [supplier_id],
                                "Expiry Flag": [expiry_flag],
                                "Created at": [today],
                                "Inventory Update Date": [other_item],
                                "Quantity in Inventory": 0,
                                "Min Quantity": [other_item],
                                "Expiry Date": [other_item],
                                "Date Sold": [other_item],
                                "Quantity Sold": [other_item]
                                }, index=[prod_id])

    # concatenate to call save file/function
    cf.concat_df(new_product)
    print(f"{new_product}\n\n .....saved ")
    print("------------------------------------------------------------------------------")
    input("\nPress enter to proceed...")


def remove_product(master_list):
    """input password
    if not password match
    print you have no authorities for this operation
    if password match
    input product ID
    call master list
    drop the item from master list

    """
