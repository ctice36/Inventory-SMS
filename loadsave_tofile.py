import pandas as pd


# File format is JSON.
def load_catalog():
    try:
        master_list = pd.read_json("Product List.json", orient='index')
        master_list.index.name = "Product ID"

    except FileNotFoundError:
        print("File not found. Initialize empty DataFrame")
        master_list = pd.DataFrame(
            columns=["Product ID", "Product Name", "Product Categories", "Product Price", "Supplier Name",
                     "Supplier ID", "Created at", "Inventory Update Date", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    except ValueError:
        print("Invalid JSON format. Initialize empty DataFrame")
        master_list = pd.DataFrame(
            columns=["Product ID", "Product Name", "Product Categories", "Product Price", "Supplier Name",
                     "Supplier ID", "Created at", "Inventory Update Date", "Quantity in Inventory", "Min Quantity",
                     "Expiry Flag", "Expiry Date", "Date Sold", "Quantity Sold"])
        master_list.set_index("Product ID", inplace=True)

    master_list[["Created at", "Inventory Update Date", "Expiry Date", "Date Sold"]] = (
        master_list[["Created at", "Inventory Update Date", "Expiry Date", "Date Sold"]].astype("object"))
    return master_list


def load_inventory(product_id):
    master_list = load_catalog()
    inventory = master_list.loc[[product_id], ["Product Name", "Inventory Update Date", "Quantity in Inventory", "Min "
                                               "Quantity", "Expiry Flag", "Expiry Date"]]
    return inventory


def load_sales():
    master_list = load_catalog()
    sales = master_list.loc[:, ["Product Name", "Product Price", "Quantity in Inventory", "Min Quantity", "Date Sold", "Quantity Sold"]]
    return sales


def merge_df(updated_list):
    master_list = load_catalog()
    master_list.update(updated_list)
    save_catalog(master_list)


def concat_df(list_to_concat):
    master_list = load_catalog()
    new_master_list = pd.concat([master_list, list_to_concat])
    save_catalog(new_master_list)


# may consider to combine save and merge
def save_catalog(list_to_save):
    # even though the column arrangement is not same is ok, as long as the name is correct
    product_list = list_to_save.sort_index()
    product_list.to_json("Product List.json", orient='index', indent=4)
