import pandas as pd
from datetime import timedelta
import loadsave_tofile as ltf
import product_catalog as pc


def update_inv(prod_id):
    product_df = ltf.load_inventory(prod_id)
    # ["Product Name", "Inventory Update Date", "Quantity in Inventory", "Expiry Date", "Min Quantity"]
    # print(f" Product_df (before):\n {product_df, type(product_df)}")

    today = pc.get_date()
    expiry_date = today
    inv_update_date = today.strftime("%Y-%m-%d")
    quantity_added = int(input("Quantity to add: "))
    min_quantity = int(input("Minimum quantity alert: "))
    print(product_df.loc[prod_id, "Expiry Flag"])

    if product_df.loc[prod_id, "Expiry Flag"] == 1:
        expiry_date = (today + timedelta(weeks=52)).strftime("%Y-%m-%d")
    elif product_df.loc[prod_id, "Expiry Flag"] == 2:
        expiry_date = (today + timedelta(weeks=36)).strftime("%Y-%m-%d")
    elif product_df.loc[prod_id, "Expiry Flag"] == 3:
        expiry_date = (today + timedelta(weeks=2)).strftime("%Y-%m-%d")

    total_quantity = int(product_df.loc[prod_id, "Quantity in Inventory"]) + quantity_added

    updated_info = {
        "Inventory Update Date": inv_update_date,
        "Quantity in Inventory": total_quantity,
        "Expiry Date": expiry_date,
        "Min Quantity": min_quantity
    }

    for col, val in updated_info.items():
        product_df.at[prod_id, col] = val

    """
    # Old coding:
    product_df.loc[prod_id, "Inventory Update Date"] = inv_update_date
    product_df.at[prod_id, "Quantity in Inventory"] = total_quantity
    product_df.at[prod_id, "Expiry Date"] = expiry_date
    product_df.at[prod_id, "Min Quantity"] = min_quantity"""

    ltf.merge_df(product_df)
    print("Merge completed")

    """
    _________________________________________________________________
    def update_inv
        print product name just to make sure adding the correct product
        input new quantity
        save today date 
        call save file
        only merge the changed data only
    
    __________________________________________________________________
    def alert_expiry
        call expiry date
    
    __________________________________________________________________
    def min_quantity
        get alert from sold 
        if the quantity in inv less than min --> alert 
    """
