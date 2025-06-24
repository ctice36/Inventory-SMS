import pandas as pd
import check_info as ci

# File format is JSON.
_files_cache = {}


def refresh_catalog(filename):
    if filename in _files_cache:
        del _files_cache[filename]


def load_file(filename):
    if filename in _files_cache:  # To make sure the file downloaded only once
        return _files_cache[filename]

    product_list = 0

    try:
        product_list = pd.read_json(filename, orient='index')
        product_list.index.name = "Product ID"

        # to change all date related column to string
        for col in product_list.columns:
            if "date" in col.lower():
                product_list[[col]] = product_list[[col]].astype("object")

    except (FileNotFoundError, ValueError):
        # any date related column must have "date" in its name
        match filename:
            case "Product List.json":  # Match product list columns
                print("Creating new Product List file.")
                product_list = pd.DataFrame(columns=["Product ID",
                                                     "Product Name",
                                                     "Product Categories",
                                                     "Product Price",
                                                     "Supplier Name"
                                                     "Supplier ID",
                                                     "Expiry Flag",
                                                     "Register Date"])
                product_list.set_index("Product ID", inplace=True)

            case "Inventory.json":  # Match inventory columns
                print("Creating new Inventory file.")
                product_list = pd.DataFrame(columns=["Product ID",
                                                     "Product Name",
                                                     "Product Price",
                                                     "Expiry Flag",
                                                     "Batch Date",
                                                     "Expiry Date",
                                                     "Inventory Quantity",
                                                     "Minimum Quantity"])
                product_list.set_index("Product ID", inplace=True)
            # Do we really need to create blank sales record ?????=============
            case "Sales Record.json":  # Match sales record columns
                print("Creating new Sales Record file.")
                product_list = pd.DataFrame(columns=["Product ID",
                                                     "Quantity Sold",
                                                     "Transaction Date",
                                                     "Promotion"])
                product_list.set_index("Product ID", inplace=True)

    return product_list


def main_info():
    master_list = load_file("Product List.json")
    main_list = master_list.loc[:, ["Product Name",
                                    "Product Price",
                                    "Expiry Flag"]]

    return main_list


def load_inventory():
    inv_list = load_file("Inventory.json")
    main_list = main_info()

    if len(inv_list.index) < len(main_list.index):
        df = ci.inv_check(inv_list, main_list)
        return df
    else:
        return inv_list


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
