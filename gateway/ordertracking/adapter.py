import requests
import os

class OrderService:
    order_tracking_url: str


    def __init__(self):
        order_tracking_service_ip = os.getenv("ORDER_TRACKING_SERVICE_IP")
        order_tracking_service_port = os.getenv("ORDER_TRACKING_SERVICE_PORT")
        order_tracking_service_protocol = os.getenv("ORDER_TRACKING_SERVICE_PROTOCOL")
        self.order_tracking_service_url = f"{order_tracking_service_protocol}://{order_tracking_service_ip}:{order_tracking_service_port}"


    def get_all_orders(self, user_id):
        orders = requests.get(
            f"{self.order_tracking_service_url}/orders", params={"user_id": user_id}
        )
        return orders.json()


    def get_one_order(self, order_id):
        order = requests.get(f"{self.order_tracking_service_url}/orders/{order_id}")
        return order.json()
