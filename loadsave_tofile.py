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
                     "Supplier ID", "Register on", "Batch Number", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    except ValueError:
        print("Invalid JSON format. Initialize empty DataFrame")
        master_list = pd.DataFrame(
            columns=["Product ID", "Product Name", "Product Categories", "Product Price", "Supplier Name",
                     "Supplier ID", "Register on", "Batch Number", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    master_list[["Register on", "Batch Number", "Expiry Date", "Date Sold"]] = (
        master_list[["Register on", "Batch Number", "Expiry Date", "Date Sold"]].astype("object"))
    return master_list"""
_files_cache = {}


def load_file(filename):

    if filename in _files_cache:  # To make sure the file downloaded only once
        return _files_cache[filename]

    try:
        pc_list = pd.read_json(filename, orient='index')
        pc_list.index.name = "Product ID"
        if "Register on" in pc_list.columns:
            pc_list[["Register on"]] = (pc_list[["Register on"]].astype("object"))

    except FileNotFoundError and ValueError:
        print("File not found.")
        match filename:
            case "Product List2.json":  # Match product list columns
                pc_list = pd.DataFrame(columns=["Product ID",
                                                "Product Name",
                                                "Product Categories",
                                                "Product Price",
                                                "Supplier Name"
                                                "Supplier ID",
                                                "Expiry Flag",
                                                "Register on"])
                pc_list.set_index("Product ID", inplace=True)

            case "Inventory.json":  # Match inventory columns
                pc_list = pd.DataFrame(columns=["Product ID",
                                                "Product Price",
                                                "Expiry Flag",
                                                "Batch Number",
                                                "Expiry Date",
                                                "Inventory Quantity",
                                                "Minimum Quantity"])
                pc_list.set_index("Product ID", inplace=True)
            # Do we really need to create blank sales record ?????=============
            case "Sales Record.json":  # Match sales record columns
                pc_list = pd.DataFrame(columns=["Product ID",
                                                "Quantity Sold",
                                                "Date Sold",
                                                "Promotion"])
                pc_list.set_index("Product ID", inplace=True)

    return pc_list


def load_inventory(product_id):
    inventory = load_file("Inventory.json")
    return inventory


def load_sales():
    sales = load_file("Sales.json")
    return sales


def merge_df(updated_list, filename):  # <------------------INSERT FILENAME
    master_list = load_file(filename)
    master_list.update(updated_list)
    return master_list


def concat_df(list_to_concat, filename):  # <------------------INSERT FILENAME
    master_list = load_file(filename)
    if master_list.shape[0] == 0:  # Only use once, during initialize or new file
        return list_to_concat
    else:
        new_master_list = pd.concat([master_list, list_to_concat])
        return new_master_list


# may consider to combine save and merge
def save_catalog(list_to_save, filename):  # <------------------INSERT FILENAME
    # even though the column arrangement is not same is ok, as long as the name is correct
    product_list = list_to_save.sort_index()
    product_list.to_json(filename, orient='index', indent=4)
    _files_cache[filename] = product_list


def show_list():
    master_list = load_file("Product List2.json")
    print(master_list["Product Name"])
    input("\nPress enter to proceed...")
