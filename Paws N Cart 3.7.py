# Task
# Create a shopping cart for a user to view
# Add or remove items
# Calculate the total cost of the cart

# Log
# Date: 21/12/2023
# Version: v3.7
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

#Declare initial values / dictionaries

#Make life easier for spacing
line_breaker = "=" * 10

# #Could use enumrate here instead of dictionary
# action_list = ["Add an item","Remove an item","View cart / total cost","Checkout","View our products","Exit"]
# for action_num,action in enumerate(action_list,1):
#     print(f"{action_num} : {action}")

#Dictionaries
action_dict = {1 : "Add an item",
2 : "Remove an item", 
3 : "View cart / total cost", 
4 : "Checkout",
5 : "View our products",
6 : "Exit"}

#Potentially add another dictionary to assign ref to each items and reference other formulas/list/dictionaries form there.
product_dict = {"Canned Food": 4.99, "Cat Toys" : 8.99, "Pet Snacks" : 3.99, "Bin Bags" : 1.99} 
recommendation_dict = {"Canned Food" : "Pet Snacks", "Pet Snacks" : "Canned Food"}

#Messages
welcome_message = f"{line_breaker} Welcome to Paws N Cart! {line_breaker}"

action_message = f"What would you like to do today? [Enter number 1 to {len(action_dict)}]\n"
return_message = "Returining to main menu...\n"
exit_message = "Thank you for your purchase. Wish you a meow day!"

purchase_message = "What would you like to buy? [Please enter the name of the product, or 1 to view products and 0 to return to menu]\n" # Could change to numerated list for easier entry
purchase_quantity_message = "How many would you like to buy?\n"
purchase_error_message = "Apologies, we do not have this product.\n"
additional_sale_message = "Would you like to add one of these items to your cart?[Y/N]\n"

remove_message = "What would you like to remove? [Please enter the name of the product]\n"
remove_quantity_message = "How many would you like to remove? [Please enter the quantity]\n"
remove_error_message = "This product is not in your cart."

num_error_message = "Please enter a valid number.\n"
yes_no_error = "Please enter Y to proceed or N to return to main menu.\n"

#Empty values
action = ""
cart_dict = {}
total_cost = 0
check_out_products = cart_dict.keys()
check_out_breakdown = {}


#Potential improvements
#1. Reference dictionary for products
#2. A dictionary for storage of each products
#3. Allow customer to enter reference number instead of typing the product name
#4. Potential improvement of the coding to reduce the length and improve efficiency
#5. Recommendation list - done

#Beginning
print(welcome_message)
print(f"Please see below for our range of products:\n")

#Display the range of products with prrices vertically
for product in product_dict:
    print(f"{product}\t:  \t{product_dict.get(product)}")


#Action 6 = Exit
while action != 6:

    #Declare value here to avoid accumulating values from repeating calculation (i.e. from view total)
    total_cost=0

    #If customer has completed a purchase and would like to add new items, take customer directly to add item.
    if action == 1:
        pass

    else:
        #Display actions list in vertical direction
        print(f"{line_breaker*5}\nAction List [1 to {len(action_dict)}]")
        for action_ref in action_dict:
            print(f"{action_ref}:  \t{action_dict.get(action_ref)}")

        action = input(action_message)
       
 

        #To ensure that the input is an integer and not stopping the code to run due to wrong entries.
        try:
            action = int(action)
        except ValueError:
            pass

        # #Odd bug - Integer changes back to string after coversion
        # def test_int(action):
        #     try:
        #         action = int(action)
        #         print(type(action))
        #     except ValueError:
        #         pass
        # test_int(action)
        # print(type(action))
              
        # #Another way to check for integer, if it is a number, convert it to integer, otherwise pass to else statment to print error message.
        # if action.isdigit():
        #     action = int(action)
        # else:
        #     pass

    #Add Item
    if action == 1:
        product_name = (input(purchase_message)).title()
        repeated_order = False #Set to False by default to avoid triggering the next if condition for repeated order at first run

        #Check for duplicate entries for same item as it would overwrite the current quantity. If the customer confirm that item(s) need to be removed, ask for the desired quantities.
        if product_name in cart_dict:
            
            #Check for yes/no
            while repeated_order not in ["Y","N"]:
                repeated_order = input(f"You have {cart_dict[product_name]} {product_name} in the cart. Would you like to change the quantity? [Y/N]\n").upper()
                print(yes_no_error)

            #Asking for the quantity that the customer would like to purchase
            if repeated_order == "Y":
                product_quantity = input(purchase_quantity_message)

                #Check whether input is an integer and whether it is a negative number. If so, ask for a valid number and cast it into integer.
                while not product_quantity.isdigit() or int(product_quantity) < 0:
                    product_quantity = input(num_error_message)
                cart_dict[product_name] = int(product_quantity)
                
                #If the quantity of a product is 0, remove it from the cart
                if cart_dict[product_name] == 0:
                    del cart_dict[product_name]

            #Return to purchase
            else:
                pass

        elif product_name.isdigit():
        #View products
            if int(product_name) == 1:

                #Display products available from product_dict and its price
                print(f"\n{line_breaker}Please see below for our range of products:{line_breaker}\n")
                for product in product_dict:
                    print(f"{product}\t:  \t{product_dict.get(product)}")
                print(line_breaker*5)

            #Return to main menu
            elif int(product_name) == 0:
                print(return_message)
                action = ""

            else:
                print(num_error_message)

        else:
            #Primary route for purchase - check whether product is offerred.   
            if product_name not in product_dict.keys() :
                print(purchase_error_message)
            
            #If the product is being offerred, ask for quantity.
            else:
                product_quantity = input(purchase_quantity_message)

                #Check whether the entry is an integer and whether it is a negative number. If so, ask for valid entry and cast the number to integer.
                while not product_quantity.isdigit() or int(product_quantity) < 0:
                    product_quantity = input(num_error_message)
                cart_dict[product_name] = int(product_quantity)   

                #If the quantity of a product is 0, remove it from the cart
                if cart_dict[product_name] == 0:
                    del cart_dict[product_name]  

                #Recommendation
                if product_name in recommendation_dict.keys():
                    print(f"\nYou may also like the following products\n")

                    recommend_products = recommendation_dict.get(product_name)
                    print(f"{line_breaker*5}\n{recommend_products} : {product_dict.get(recommend_products)}\n{line_breaker*5}")
                    
                    #Set additional_sale to 0 to trigger validity check for entry
                    additional_sale = 0
                    while additional_sale not in ["Y","N"]:
                        additional_sale = input(additional_sale_message).upper()
                        
                        #Direct customer to add item
                        if additional_sale == "Y":
                            action = 1
                        
                        #Return to main menu
                        elif additional_sale == "N":
                            action = ""
                            print()

                        #Reminder for valid entries
                        else:
                            print(yes_no_error)

        #Display a breakdown
        print(f"{line_breaker} Here's the items in your cart {line_breaker}\n")

        for product in cart_dict:
            print(f"{product}\t:   \t{cart_dict.get(product)}")
      
        print(f"\n{line_breaker*5}")

    #Remove an item
    elif action == 2 :
        #Display the items in the cart
        print(f"{line_breaker} Here's the items in your cart {line_breaker}\n")
            
        for product in cart_dict:
            print(f"{product}\t:   \t{cart_dict.get(product)}")
        
        print(f"\n{line_breaker*5}")
        
        #Ask for items to be removed
        remove_product = (input(remove_message)).title()

        #Check whether an item is in the cart
        if remove_product not in cart_dict:
            print(remove_error_message)

        #Ask for the quantity to be removed
        else:
            product_quantity = input(remove_quantity_message)

            #Check whether the entry is an integer, a negative number or more than what is in the cart. If so, ask for correct quantity
            while not product_quantity.isdigit() or int(product_quantity) < 0 or int(product_quantity) > cart_dict.get(remove_product):
                product_quantity = input(f"Please enter a valid number. You have {cart_dict[remove_product]} {remove_product} in your cart. [Enter 0 if you don't want to remove anything]\n")

            #Look for the product and remove the quantities entered.
            cart_dict[remove_product] -= int(product_quantity)

            #If the quantity of a product is 0, remove it from the cart
            if cart_dict[remove_product] == 0:
                del cart_dict[remove_product]

            #Display the current item(s) in the cart.
            print(f"{line_breaker}Here's the items in your cart{line_breaker}\n")
            
            for product in cart_dict:
                print(f"{product}\t:   \t{cart_dict.get(product)}")
        
            
            print(f"\n{line_breaker*5}")

    #View cart and total cost
    elif action == 3:

        #Calculation of the product cost by referencing back to the dictionaries and add to the check_out_breakdown. Quantity from cart_dict and Price from product_dict.
        for product in check_out_products:
            cost = cart_dict.get(product)*product_dict.get(product)
            
            check_out_breakdown[product] = cost
            total_cost += cost

        #Display the total cost and breakdown through referencing cart_dict for quantity, product_dict for price and check_out_breakdown for subtotal for each product
        print(f"{line_breaker} The total cost is {total_cost:.2f} {line_breaker}\n")
        
        for product in check_out_products:
            print(f"{product}   \tQuantity {cart_dict.get(product)}\t*\t{product_dict.get(product)}  \tCost {check_out_breakdown.get(product)}")

        print(f"\n{line_breaker*5}")

    #Checkout
    elif action == 4:
        
        #Calculate the product cost by referencing cart_dict for quantity and product_dict for price then store the data in check_out_breakdown with the total added together.
        for product in check_out_products:
            cost = cart_dict.get(product)*product_dict.get(product)
            
            check_out_breakdown[product] = cost
            total_cost += cost

        #Display breakdown with reference same as line 147
        print(f"{line_breaker} Receipt Details {line_breaker}\n")

        for product in check_out_products:
            print(f"{product}   \tQuantity {cart_dict.get(product)}\t*\t{product_dict.get(product)}  \tCost {check_out_breakdown.get(product)}")

        print(f"\nThe total cost is {total_cost:.2f}\n")
        print(line_breaker*5)

        #Default check_out value to 0 to trigger the while loop for checking valid entry
        check_out = 0

        #Check whether entry is valid
        while check_out not in ["Y","N"]:
            check_out = (input(f"Would you like to check out? [Y/N]\n")).upper()
            
            #Complete the purchase and return to main menu
            if check_out == "Y":
                print(f"\n{exit_message}\n{line_breaker*5}")
                action = 6

            #Return to main menu
            elif check_out == "N":
                print(return_message)

            #Reminder for valid entries
            else:
                print(yes_no_error)

    #View products
    elif action == 5:
        
        #Display products available from product_dict and its price
        print(f"\n{line_breaker}Please see below for our range of products:{line_breaker}\n")
        for product in product_dict:
            print(f"{product}\t:  \t{product_dict.get(product)}")
        print(line_breaker*5)

    #Exit
    elif action == 6:
        print(f"\n{exit_message}\n{line_breaker*5}")


    #Reminder for valid action entries
    else:
        print(f"{line_breaker} Please enter the number 1 to {len(action_dict)} {line_breaker}\n")
