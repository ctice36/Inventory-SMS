import loadsave_tofile as ltf
import pandas as pd


def id_check(must_exist=True):
    while True:

        master_list = ltf.main_info().index
        print("Input the Product ID")
        product_id_input = input("Product ID: ").upper().strip()  # Product ID / Bar Code
        exist = product_id_input in master_list.values

        if not must_exist and exist:
            print(f"{product_id_input} has been registered")

        elif must_exist and not exist:
            print(f"{product_id_input} is not registered yet")

        else:
            return product_id_input

        print("\nDo you want to:")
        print(f"1. Re-input the product id?")
        print("2. Go back to the main menu?")
        while True:
            try:
                proceed_or_not = int(input("= "))
                if proceed_or_not == 1:
                    break  # to repeat checking product_id while loop
                elif proceed_or_not == 2:
                    print("Going back to main menu")
                    return None
                else:
                    print("Invalid input. Please choose a number between 1 or 2")
                    continue
            except ValueError:
                print("Invalid input. Please choose a number between 1 or 2")
                continue


def inv_check(inv_list, main_list):

    if len(inv_list.index) == 0:
        return main_list
    elif 0 < len(inv_list.index) < len(main_list.index):
        merging = pd.merge(main_list, inv_list, on="Product ID", how="outer", indicator=True)
        pd.set_option('display.max_columns', None)
        # print(f"Before \n {merging}")
        if not merging[merging["_merge"] == "right_only"].empty:
            # The right_only should not exist
            print("The Product List file is corrupt. Please check and repair manually")
            return None
        elif not merging[merging["_merge"] == "left_only"].empty:
            # The left_only means the product catalog is not updated to inventory
            only_left = merging[~(merging["_merge"] == "both")]
            only_left = only_left.drop(columns=[col for col in only_left.columns if col.endswith("_y")] + ["_merge"]) \
                .rename(columns={col: col.replace("_x", "") for col in only_left.columns if col.endswith("_x")})
            # print(f"'both' deleted \n {only_left}")
            inv_list = pd.concat([inv_list, only_left])
            # print(f"Concat INV lst \n {inv_list}")
            return inv_list
