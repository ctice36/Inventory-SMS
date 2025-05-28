import pandas as pd
import loadsave_tofile as cf
import datetime as dt


def get_date():
    return dt.datetime.today()


# Return the new df of a new product
def add_product(prod_id):
    # prod_id = input(f"Product ID: ").capitalize().strip()  # product id / bar code: unique for each product
    prod_name = input(f"Product Name: ").title().strip()
    prod_category = input(f"Product Categories: ").title().strip()
    prod_price = float(input(f"Product Price (per unit): RM"))
    supplier_name = input(f"Supplier Name: ").title().strip()
    supplier_id = input(f"Supplier ID: ").capitalize().strip()
    print(f"Please input the expiry code")
    print(f"1. Non-expire prod")
    print(f"2. More than 1 year.")
    print(f"3. Expire within 1 year")
    expiry_flag = int(input(f"Expiry code: "))
    today = get_date().strftime("%Y-%m-%d")

    new_product = pd.DataFrame({"Product Name": [prod_name],
                                "Product Categories": [prod_category],
                                "Product Price": [prod_price],
                                "Supplier Name": [supplier_name],
                                "Supplier ID": [supplier_id],
                                "Expiry Flag": [expiry_flag],
                                "Created at": [today],
                                }, index=[prod_id])

    # Call the master list, concatenate and call save file/function

    cf.merge_df(new_product)
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
