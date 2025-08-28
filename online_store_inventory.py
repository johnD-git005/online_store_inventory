store = {
	"Laptop": {"price": 1200, "quantity": 5},
	"Headphones": {"price": 150, "quantity": 10},
	"Mouse": {"price": 40, "quantity": 40}
	}

# START FUNCTION
def start():
	while True:
		print("""
		1. ADD PRODUCTS
		2. UPDATE STOCK
		3. SELL A PRODUCT
		4. DISPLAY INVENTORY
		5. MOST EXPENSIVE PRODUCT
		6. TOTAL POTENTIAL SALES
		7. TERMINATE PROGRAM
		""")

		option = int(input("\n Select Option: "))
		call_function(option)

# FUNCTION TO CALL IF, ELIF AND ELSE STATEMENT
def call_function(user_choice):
	if user_choice == 1:
		print("\n ADD NEW PRODUCT")
		name = input("\n Enter Product Name: ").capitalize().strip()
		price = int(input("\n Enter Product Price: "))
		quantity = int(input("\n Enter Product Quantity: "))
		add_products(name, price, quantity)
		print(f"\n {store}")

	elif user_choice == 2:
		print("\n UPDATE STOCK")
		update = input("\n Enter Product Name: ").capitalize().strip()
		update_stock(update)

	elif user_choice == 3:
		print("\n Sell A Product")
		product_name = input("\n Enter Product Name: ").capitalize().strip()
		sell_a_product(product_name)

	elif user_choice == 4:
		print("\n DISPLAY INVENTORY")
		display_inventory(store)

	elif user_choice == 5:
		most_expensive_product(store)

	elif user_choice == 6:
		total_potential_sales(store)	

	elif user_choice == 7:
		terminate_program()
	
	else:
		print("\n Invalid Choice")

# FUNCTION TO ADD PRODUCTS
def add_products(name, price, quantity):
	if name in store:
		print(f"\n Product: {name} already exists in the store")
		print(f"\n {name}:{store[name]}")
	else:
		store[name] = {
			"price": price,
			"quantity": quantity
			}
		print(f"\n New Product Added Successfully!")
		print(f"\n Product Name:{name}, Price:{price}, Quantity:{quantity}")

# FUNCTION TO UPDATE STOCK
def update_stock(product):
	if product in store:
		print(f"\n {product}:{store[product]}")
		print("""
		1. UPDATE PRICE
		2. UPDATE QUANTITY
		""")
		
		option = int(input("\n Select an Option to continue: "))		
		if option == 1:
			print("\n UPDATE PRICE")
			new_price = int(input("\n Enter New Price: "))
			store[product].update({"price":new_price})
			print(f"\n {product} Price successfully updated")
			print(f"\n {product}:{store[product]}")

		elif option == 2:
			print("\n UPDATE QUANTITY")
			new_quantity = int(input("\n Enter New Quantity: "))
			old_quantity = store[product]["quantity"]
			old_quantity += new_quantity
			store[product].update({"quantity": old_quantity})
			print(f"\n {product} Quantity successfully updated")
			print(f"\n {product}:{store[product]}")
		else:
			print("\n Invalid Selection")
	else:
		print("\n Product not Found!")

# FUNCTION TO SELL A PRODUCT	
def sell_a_product(product):
	if product not in store:
		print("\n Product Is Out of Stock!")

	else:
		print(f"\n {product}:{store[product]}")
		quantity = int(input("\n Quntity of Product to Sell: "))

		if quantity > store[product]["quantity"]:
			print("\n Not Enough Quantity. Stock is Insufficient!")
		
		elif quantity < 0 or quantity == 0:
			print("\n Please Input a Valid Number for Quantity")

		else:
			old_quantity = store[product]["quantity"]
			old_quantity -= quantity
			store[product].update({"quantity": old_quantity})
			print(f"\n Product Name: {product}, Quantity Sold: {quantity}")
			print(f"\n {product}:{store[product]}")
			print(f"\n SUMMARY OF TOTAL SALES")
			price = store[product]["price"]
			price *= quantity
			print(f"\n Number of Product Sold: {quantity}, Total Price: {price}")
			
# FUNCTION TO DISPLAY INVENTORY
def display_inventory(store_dict):
	for items in store_dict:
		price = store_dict[items]["price"]
		quantity = store_dict[items]["quantity"]
		print(f"\n Product Name: {items}, Price: {price}, Quantity: {quantity}")
	print(f"\n TOTAL NUMBER OF PRODUCTS DISPLAY: {len(store_dict)}")


# FUNCTION TO DISPLAY MOST EXPENSIVE PRODUCT
def most_expensive_product(store_dict):
	expensive = []
	for items in store_dict:
		expensive.append(store_dict[items]["price"])

	most_expensive = expensive[0]
	for costly_items in expensive:
		if costly_items > most_expensive:
			most_expensive = costly_items

	for product in store_dict:		
		product_price = store_dict[product]["price"]
		if most_expensive == product_price:
			print(f"\n MOST EXPENSIVE PRODUCT {product}:{store_dict[product]}")
		

# FUNCTION TO DISPLAY TOTAL POTENTIAL SALES
def total_potential_sales(store_dict):
	total_value = 0
	for sales in store_dict:
		if store_dict[sales]["quantity"] <= 0:
			continue

		else:
			total_price = store_dict[sales]["price"]
			total_value += total_price
			print(f"REMAINING STOCK FOR: {sales}:{store_dict[sales]}")
	print(f"\n TOTAL VALUE OF REMAINING STOCK: {total_value}")
	

# FUNCTION TO TERMINATE PROGRAM
def terminate_program():
	print("\n Terminating Program. Goodbye!")
	exit()

start()
