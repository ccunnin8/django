def objects():
    return {
        1: {
            "product": "Television",
            "price": 7.99,
            "id": 1
        },
        2: {
            "product": "Speakers",
            "price": 12.99,
            "id": 2
        },
        3: {
            "product": "Computer",
            "price": 5.99,
            "id": 3
        },
        4: {
            "product": "Controller",
            "price": 4.99,
            "id": 4
        },
        5: {
            "product": "iPhone",
            "price": 799.99,
            "id": 5
        }
    }

def get_products():
    products_data = []
    products = objects()
    for product in products:
        products_data.append(products[product])
    return products_data

def get_product(id):
    products = objects()
    return products[id]
