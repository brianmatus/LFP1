class Restaurant:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories


class Category:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements


class Product:
    def __init__(self, name, real_name, description, price):
        self.name = name
        self.real_name = real_name
        self.description = description
        self.price = price


class ShoppedProduct:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class ParseError:
    def __init__(self, row, index, msg):
        self.row = row
        self.index = index
        self.msg = msg


class Order:
    def __init__(self, client_name, nit, address, tip, shopped_products):
        self.client_name = client_name
        self.nit = nit
        self.address = address
        self.tip = tip
        self.shopped_products = shopped_products
