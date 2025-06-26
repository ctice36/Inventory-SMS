import pandas as pd
from datetime import timedelta
import loadsave_tofile as ltf
import product_catalog as pc
import check_info as ci


def update_inv():
    # ["Product ID", "Product Price", "Expiry Flag", "Batch Date", "Expiry Date",
    # "Inventory Quantity", "Minimum Quantity"]

    inv_list = ltf.load_inventory()
    today = pc.get_date()
    expiry_date = today
    batch_no = today.strftime("%Y%m%d")

    while True:
        """↓↓↓↓　Do this checking needed as we load all product from inv list here"""
        prod_id = ci.id_check(must_exist=True)
        if prod_id is None:
            return

        update_target = inv_list.loc[[prod_id]]
        print(update_target)

        quantity_added = int(input("Added quantity: "))
        # print(update_target.loc[prod_id, "Expiry Flag"])
        min_quantity = 0

        if update_target.loc[prod_id, "Expiry Flag"] == 1:
            expiry_date = (today + timedelta(weeks=52)).strftime("%Y-%m-%d")
            min_quantity = int(quantity_added * 0.1)

        elif update_target.loc[prod_id, "Expiry Flag"] == 2:
            expiry_date = (today + timedelta(weeks=36)).strftime("%Y-%m-%d")
            min_quantity = int(quantity_added * 0.2)

        elif update_target.loc[prod_id, "Expiry Flag"] == 3:
            expiry_date = (today + timedelta(weeks=2)).strftime("%Y-%m-%d")
            min_quantity = int(quantity_added * 0.3)

        total_quantity = quantity_added
        if "Inventory Quantity" in update_target.columns:
            if update_target.loc[prod_id, "Inventory Quantity"] is not None:
                total_quantity = update_target.loc[prod_id, "Inventory Quantity"] + quantity_added

        updated_info = {
            "Batch Date": batch_no,
            "Inventory Quantity": total_quantity,
            "Expiry Date": expiry_date,
            "Min Quantity": min_quantity
        }
        # print(updated_info)

        for col, val in updated_info.items():
            if col not in inv_list.columns:
                inv_list[col] = None
            inv_list.at[prod_id, col] = val

        next_pd = input("Continue for next product? Y/N - ").capitalize()
        match next_pd:
            case "Y":
                continue
            case "N":
                break
            case _:
                print("Invalid input. Input only Y or N")
        # Nothing will be run after this line

    print(f"\nPrinted outside while loop\n{inv_list[:prod_id]}")
    list_to_save = ltf.concat_df(inv_list[:prod_id],"Inventory.json")
    ltf.save_catalog(list_to_save,"Inventory.json")





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
