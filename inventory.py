import pandas as pd
import loadsave_tofile as ltf


def update_inv(prod_id):
    product_df = ltf.load_inventory(prod_id)
    # Prod ID | Prod Name | Inventory update Date | Quantity in Inv

    """
    print product name just to make sure adding the correct product
    input new quantity
    save today date 
    call save file
    only merge the changed data only
    
    
    """
