import pandas as pd
from datetime import timedelta
import loadsave_tofile as ltf
import product_catalog as pc


def load_sales_df():
    return ltf.load_sales()

def multiple(quantity, price):
    return quantity * price

def add(total, multiplied_price):
    return total + multiplied_price

def minus_from_inv(inv_qtt, trans_qtt):
    return inv_qtt - trans_qtt

def transaction():
    sale_df = ltf.load_sales()
    today = pc.get_date().strftime("%Y-%m-%d")
    product_id = input("Product ID: ")

    while True:

        try:
            if product_id not in sale_df.index.values:
                print("The product is not available")
            else:
                break
        except ValueError:
            print("Input the correct product ID")
            continue

    trans_df = sale_df.loc[[product_id], ["Product Name", "Product Price", "Quantity in Inventory", "Date Sold",
                                          "Quantity Sold"]]
    print(f"Product name: {trans_df[product_id, "Product Price"]}")
    trans_qtt = int(input("Quantity: "))

    price = trans_df[product_id, "Product Price"]
    inv_qtt = trans_df[product_id, "Quantity in Inventory"]

    qtt_x_price = multiple(trans_qtt, price)
    left_in_inv = minus_from_inv(inv_qtt, trans_qtt)

    updated_info = {
        "Quantity in Inventory": left_in_inv,
        "Date Sold": today,
        "Quantity Sold": trans_qtt
    }

    for col, val in updated_info.items():
        trans_df.at[product_id, col] = val


"""

should I make a different file for sales_transaction only?
as I might want to print the sales performance?
conclusion: make a separate file. one for catalog. one for inv and sales record
 


call today date
call df for sold
input product code
input trans quantity 
minus quantity in inv
quantity * price



"""
