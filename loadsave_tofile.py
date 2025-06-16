import pandas as pd

# File format is JSON.
"""def load_catalog():
    try:
        master_list = pd.read_json("Product List.json", orient='index')
        master_list.index.name = "Product ID"

    except FileNotFoundError:
        print("File not found. Initialize empty DataFrame")
        master_list = pd.DataFrame(
            columns=["Product ID", "Product Name", "Product Categories", "Product Price", "Supplier Name",
                     "Supplier ID", "Created at", "Batch Number", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    except ValueError:
        print("Invalid JSON format. Initialize empty DataFrame")
        master_list = pd.DataFrame(
            columns=["Product ID", "Product Name", "Product Categories", "Product Price", "Supplier Name",
                     "Supplier ID", "Created at", "Batch Number", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    master_list[["Created at", "Batch Number", "Expiry Date", "Date Sold"]] = (
        master_list[["Created at", "Batch Number", "Expiry Date", "Date Sold"]].astype("object"))
    return master_list"""


def load_catalog(filename):
    try:
        pc_list = pd.read_json(filename, orient='index')
        pc_list.index.name = "Product ID"
        pc_list[["Created at"]] = (pc_list[["Created at"]].astype("object"))

    except FileNotFoundError:
        print("File not found.")
        pc_list = pd.DataFrame(
            columns=["Product ID",
                     "Product Name",
                     "Product Categories",
                     "Product Price",
                     "Expiry Flag"])
        pc_list.set_index("Product ID", inplace=True)

    except ValueError:
        print("Invalid JSON format. Initialize empty DataFrame")
        pc_list = pd.DataFrame(
            columns=["Product ID",
                     "Product Name",
                     "Product Categories",
                     "Product Price",
                     "Expiry Flag"])
        pc_list.set_index("Product ID", inplace=True)

    return pc_list


def load_inventory(product_id):
    master_list = load_catalog("Inventory.json")
    inventory = master_list.loc[[product_id], ["Batch Number",
                                               "Expiry Flag"]]
    return inventory


def load_sales():
    master_list = load_catalog("Sales.json")
    sales = master_list.loc[:, ["Product Name",
                                "Product Price",
                                "Quantity in Inventory",
                                "Min Quantity",
                                "Date Sold",
                                "Quantity Sold"]]
    return sales


def merge_df(updated_list, filename):  # <------------------INSERT FILENAME
    master_list = load_catalog(filename)
    master_list.update(updated_list)
    return master_list


def concat_df(list_to_concat, filename):  # <------------------INSERT FILENAME
    master_list = load_catalog(filename)
    if master_list.shape[0] == 0:  # Only use once, during initialize or new file
        return list_to_concat
    else:
        new_master_list = pd.concat([master_list, list_to_concat])
        return new_master_list


# may consider to combine save and merge
def save_catalog(list_to_save, filename): # <------------------INSERT FILENAME
    # even though the column arrangement is not same is ok, as long as the name is correct
    product_list = list_to_save.sort_index()
    product_list.to_json(filename, orient='index', indent=4)
