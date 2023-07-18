from flask import Blueprint
from models.order_list import Order

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/order")
def index():
  return "<h1>I will show all the orders</h1>"
