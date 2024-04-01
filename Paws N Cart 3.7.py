# Task
# Create a shopping cart for a user to view
# Add or remove items
# Calculate the total cost of the cart

# Log
# Date: 01/04/2024
# Version: v3.8.1
# Update: 
#   v1.0 Drafted on List
#   v2.0 Introduction of Dictionary
#   v2.5 Add comments & tidy up the code
#   v3.0 Added Integer Checks
#   v3.1 Referencing messages from the top
#   v3.2 Add recommendation
#   v3.3 Direct customer from recommendation to add item
#   v3.4 Tidy up display for customers & coding structure
#   v3.5 Add return function from purchasing
#   v3.6 Remove display of items with 0 quantity
#   v3.7 Add Yes/No check to repeated order question
#   v3.8.1 Revised the code to use Definition and OOP  

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.total_cost = 0

    def add_item(self, product_name, product_quantity, product_dict):
        if product_name in product_dict:
            self.cart[product_name] = product_quantity
        else:
            print("Apologies, we do not have this product.")

    def remove_item(self, product_name, product_quantity):
        if product_name in self.cart:
            if product_quantity < self.cart[product_name]:
                self.cart[product_name] -= product_quantity
            else:
                del self.cart[product_name]
        else:
            print("This product is not in your cart.")

    def view_cart(self):
        print("=" * 10 + " Here's the items in your cart " + "=" * 10)
        for product, quantity in self.cart.items():
            print(f"{product}\t:   \t{quantity}")
        print("=" * 45)

    def checkout(self, product_dict):
        self.total_cost = sum(self.cart[product] * product_dict[product] for product in self.cart)
        print("=" * 10 + " Receipt Details " + "=" * 10)
        for product, quantity in self.cart.items():
            cost = quantity * product_dict[product]
            print(f"{product}\t:   \tQuantity {quantity}\t*\t{product_dict[product]}\tCost {cost}")
        print(f"\nThe total cost is {self.total_cost:.2f}")
        print("=" * 45)
        return self.total_cost


def main():
    line_breaker = "=" * 10
    action_dict = {1: "Add an item", 2: "Remove an item", 3: "View cart / total cost", 4: "Checkout",
                   5: "View our products", 6: "Exit"}
    product_dict = {"Canned Food": 4.99, "Cat Toys": 8.99, "Pet Snacks": 3.99, "Bin Bags": 1.99}
    recommendation_dict = {"Canned Food": "Pet Snacks", "Pet Snacks": "Canned Food"}

    cart = ShoppingCart()

    print(f"{line_breaker} Welcome to Paws N Cart! {line_breaker}")
    print("Please see below for our range of products:")
    for product, price in product_dict.items():
        print(f"{product}\t:  \t{price}")

    while True:
        print(f"{line_breaker*5}\nAction List [1 to {len(action_dict)}]")
        for action_ref in action_dict:
            print(f"{action_ref}:  \t{action_dict[action_ref]}")

        action = input("What would you like to do today? [Enter number 1 to 6]\n")

        try:
            action = int(action)
        except ValueError:
            pass

        if action == 1:
            product_name = input("What would you like to buy?\n").title()
            product_quantity = int(input("How many would you like to buy?\n"))
            cart.add_item(product_name, product_quantity, product_dict)
        elif action == 2:
            product_name = input("What would you like to remove?\n").title()
            product_quantity = int(input("How many would you like to remove?\n"))
            cart.remove_item(product_name, product_quantity)
        elif action == 3:
            cart.view_cart()
        elif action == 4:
            total_cost = cart.checkout(product_dict)
            if total_cost:
                checkout = input("Would you like to check out? [Y/N]\n").upper()
                if checkout == "Y":
                    print("Thank you for your purchase. Have a meow day!")
                    break
        elif action == 5:
            print(f"\n{line_breaker}Please see below for our range of products:{line_breaker}")
            for product, price in product_dict.items():
                print(f"{product}\t:  \t{price}")
        elif action == 6:
            print("Thank you for visiting Paws N Cart. Goodbye!")
            break
        else:
            print(f"{line_breaker} Please enter a number from 1 to {len(action_dict)} {line_breaker}\n")


if __name__ == "__main__":
    main()
