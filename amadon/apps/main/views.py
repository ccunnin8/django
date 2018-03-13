from django.shortcuts import render, HttpResponse, redirect
from . import data

# Create your views here.
#renders '/' with index.html, and products from simulated database
def index(req):
    return render(req,'main/index.html',{"products":data.get_products()})

#get product from 'database' with id, get price and multiply times qty
def buy(req):
    #get product id and gty from post data
    product_id = int(req.POST["product_id"])
    quantity = int(req.POST["qty"])
    #get product from database
    product = data.get_product(product_id)
    #create order_history if not in session
    if "order_history" not in req.session:
        req.session["order_history"] = []
    #add order to history in session
    order_history = req.session["order_history"]
    order_history.append({ "qty": quantity, "price": product["price"]})
    req.session["order_history"] = order_history
    #add current order to session
    req.session["current_order"] = { "qty": quantity, "price": product["price"] }
    return redirect('/confirmation')

def confirmation(req):
    #get current order from session
    order = req.session["current_order"]
    #total price is the price of the product times qty
    total_price = round(order["qty"] * order["price"],2)
    #set variables num_items, total_spend
    num_items = 0
    total_spend = 0
    #loop through order_history and get total and num_itmes
    for order in req.session["order_history"]:
        total_spend += (order["qty"] * order["price"])
        num_items += order["qty"]
    #create dictionary to use in template
    data = {
        "num_items": order["qty"],
        "total_price": total_price,
        "total_spend": round(total_spend,2)
    }
    #render confirmation template
    return render(req,'main/confirm.html',data)
