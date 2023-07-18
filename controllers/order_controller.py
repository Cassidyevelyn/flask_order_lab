from flask import Blueprint

order_blueprint("order", __name__)

@order_blueprint.route("/order")
def index():
  return "<h1>I will show all the orders</h1>"
