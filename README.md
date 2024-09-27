# Terminal-Based E-Commerce System

A Python-based terminal e-commerce system where users can register, log in, browse products, add items to their cart, place orders, and view their order history. The system stores data for users and products using JSON files and supports user authentication with password encryption, using a secure key stored separately.

## Features

- User Registration & Login: New users can register with a unique username and password. Existing users can log in using their credentials.
- View Products: Users can view available products with pricing and stock information.
- Add Products to Cart**: Users can add products to their shopping cart, with stock validation.
- Place Orders: Users can place orders for items in their cart, and stock is updated accordingly.
- Order History: Users can view their past orders.
- Product Management**: Products are managed via a JSON file, which supports stock updates and changes.
- Secure Storage**: User passwords are encrypted and decrypted using a key stored in a separate secure storage folder.

## Project Structure

```bash
.
├── main.py                # Main script to run the system
├── users.json             # JSON file to store user data (passwords are encrypted)
├── secure_storage/        # Folder containing the encryption key
│   └── key.key            # Key file for encrypting and decrypting user passwords
├── utils/
│   ├── products.json      # JSON file containing product data
│   └── helper.py          # Helper functions for password encryption and decryption
└── README.md              # Project documentation
