import queue

order_queue = queue.Queue()


def add_product_to_queue(name, quantity) -> dict:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    order = {
        "product_name": name,
        "quantity": quantity
    }
    order_queue.put(order)
    print(f"Order: {order}, added to queue")
    return order


def get_first_product_from_queue() -> dict:
    if not order_queue.empty():
        order = order_queue.get()
        print(f"Get product name: {order["product_name"]}")
        return order
    else:
        print("Queue empty")
        return {}


def watch_all_orders_in_queue() -> list:
    orders = list(order_queue.queue)
    print(f"Current orders in queue: {orders}")
    return orders


def clear_orders() -> bool:
    with order_queue.mutex:
        order_queue.queue.clear()
    print("Now queue is cleared")
    return True


def menu() -> None:
    while True:
        print("\n=== Order Management Menu ===")
        print("1. Add product to queue")
        print("2. Get first product from queue")
        print("3. See all order")
        print("4. Clear orders queue")
        print("5. Exit")
        print("Github-hook test")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            add_product_to_queue(product_name, quantity)
        elif choice == "2":
            get_first_product_from_queue()
        elif choice == "3":
            watch_all_orders_in_queue()
        elif choice == "4":
            clear_orders()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    menu()
