import json
import os
from utils.helper import encrypt_password, decrypt_password, generate_key

# Call this once to generate the key
# Uncomment this line to generate the key if it hasn't been created yet
# generate_key()

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.product_id}: {self.name} - ${self.price:.2f} (Stock: {self.stock})"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.order_history = []

    def add_to_cart(self, product):
        if product.stock > 0:
            self.cart.append(product)
            product.stock -= 1  # Decrease stock when added to cart
            print(f"{product.name} added to cart.")
        else:
            print("Sorry, this product is out of stock!")

    def place_order(self):
        if len(self.cart) == 0:
            print("Your cart is empty!")
            return
        self.order_history.append(self.cart[:])  # Copy current cart to order history
        self.cart.clear()
        print("Order placed successfully!")

    def view_order_history(self):
        if not self.order_history:
            print("No orders placed yet.")
            return
        print("Order History:")
        for index, order in enumerate(self.order_history, start=1):
            print(f"Order {index}:")
            for product in order:
                print(f"  - {product}")

class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.users = {}
        self.load_users()

    def add_product(self, product):
        self.products.append(product)

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                users_data = json.load(f)
                for username, user_info in users_data.items():
                    decrypted_password = decrypt_password(user_info['password'].encode())
                    self.users[username] = User(username, decrypted_password)

    def save_users(self):
        users_data = {}
        for username, user in self.users.items():
            encrypted_password = encrypt_password(user.password).decode()
            users_data[username] = {'password': encrypted_password}
        with open('users.json', 'w') as f:
            json.dump(users_data, f)

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists!")
            return
        self.users[username] = User(username, password)
        self.save_users()
        print("User registered successfully!")

    def login_user(self, username, password):
        if username not in self.users:
            print("User not found!")
            return None
        user = self.users[username]
        if user.password != password:
            print("Incorrect password!")
            return None
        print(f"Welcome, {username}!")
        return user

def main():
    system = ECommerceSystem()
    # Adding some sample products
    system.add_product(Product("001", "Laptop", 999.99, 10))
    system.add_product(Product("002", "Smartphone", 499.99, 5))
    system.add_product(Product("003", "Tablet", 299.99, 0))  # Out of stock for testing

    while True:
        print("\n--- E-Commerce System ---")
        print("1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = system.login_user(username, password)
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Add Product to Cart")
                    print("2. Place Order")
                    print("3. View Order History")
                    print("4. Logout")
                    sub_choice = input("Choose an option: ")

                    if sub_choice == '1':
                        product_id = input("Enter product ID: ")
                        product = next((p for p in system.products if p.product_id == product_id), None)
                        if product:
                            user.add_to_cart(product)
                        else:
                            print("Product not found!")
                    elif sub_choice == '2':
                        user.place_order()
                    elif sub_choice == '3':
                        user.view_order_history()
                    elif sub_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("\nAvailable Products:")
            for product in system.products:
                print(product)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
