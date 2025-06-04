import pandas as pd
from datetime import timedelta
import loadsave_tofile as ltf
import product_catalog as pc


def load_sales_df():
    sales = ltf.load_sales()


def multiple(quantity, price):
    return quantity * price


def add(multiplied_price):
    multiplied_price += multiplied_price
    return multiplied_price


def minus_from_inv():
    pass


"""
call today date
call df for sold
product code
quantity in inv
quantity * price



"""
