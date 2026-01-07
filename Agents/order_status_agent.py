# import the regular expressions module for pattern matching
import re

class OrderStatusAgent:
    def __init__(self, orders: dict | None = None):
        
        # mock order database
        self.orders = orders or {
            "1111": "Your order is shipped. Expected delivery in 2 days.",
            "1212": "Your order been processed. It will ship tomorrow.",
            "1313": "Your order is ready for pick up."
        }

    def handle(self, query: str) -> str:
        
        # extracts an order ID from the user query and returns its status
        query = query.lower().strip()

        # match exactly 4-digit order IDs
        match = re.search(r"\b\d{4}\b", query)

        if not match:
            return "Please provide a valid 4-digit order ID."
        
        # extract matched order ID
        order_id = match.group()
        
        # look up the order in the database
        status = self.orders.get(order_id)
        if not status:
            return f"Order {order_id} was not found."
        
        # return the order status
        return f"Order {order_id} status: {status}"
