store_dict = {
	"Laptop": {"price": 1200, "quantity": 5},
	"Headphones": {"price": 1500, "quantity": 10},
	"Mouse": {"price": 40, "quantity": 40}
	}

# FUNCTION TO START THE PROGRAM
def start_program():
	while True:
		print("""
		WELCOME TO OUR ONLINE STORE INVENTORY \v
		1. ADD PRODUCTS
		2. UPDATE STOCK
		3. SELL A PRODUCT
		4. DISPLAY INVENTORY
		5. MOST EXPENSIVE PRODUCT
		6. TOTAL POTENTIAL SALES
		7. TERMINATE PROGRAM
		""")

		user_option = input("\n Please Select an Option to continue: ")
		statements(user_option)

# FUNCTION FOR IF, ELIF AND ELSE STATEMENT
def statements(option):
	if option == "1":
		print("\n ADD PRODUCT")
		name = input("\n Enter Name of Product: ").capitalize().strip()
		price = float(input("\n Enter Price: "))
		quantity = int(input("\n Enter Quantity: "))
		add_product(store_dict, name, price, quantity)

	elif option == "2":
		print("\n UPDATE A STOCK")
		name = input("\n Enter Name of Product: ").capitalize().strip()
		quantity = int(input("\n Enter Quantity: "))
		update_stock(store_dict, name, quantity)

	elif option == "3":
		print("\n SELL A PRODUCT")
		name = input("\n Enter Name of Product: ").capitalize().strip()
		quantity = int(input("\n Enter Quantity: "))
		sell_product(store_dict, name, quantity)

	elif option == "4":
		print("\n DISPLAY INVENTORY")
		display_inventory(store_dict)

	elif option == "5":
		print("\n MOST EXPENSIVE PRODUCT")
		most_expensive_product(store_dict)

	elif option == "6":
		print("\n TOTAL POTENSTIAL SALES")
		total_potential_sales(store_dict)

	elif option == "7":
		terminate_program()

	else:
		print("\n Invalid Choice")

# FUNCTION TO ADD PRODUCTS
def add_product(store_dict, name, price, quantity):
	if name in store_dict:
		print(f"\n {name} Already Exists!")
	
	else:
		store_dict[name] = {
			"price": price,
			"quantity": quantity
			}

		print(f"\n New Product Added Successfully!")
		print(f"\n Product Name: {name}, Price: {price}, Quantity: {quantity}")

# FUNCTION TO UPDATE STOCK
def update_stock(store_dict, name, quantity):
	print("\n UPDATE STOCK")
	if name in store_dict:
		if quantity <= 0:
			print("\n Quantity must be greater than zero!")

		else:
			print(f"\n {name}: {store_dict[name]}")
			store_dict[name]["quantity"] += quantity
			print(f"\n {name} Quantity successfully updated")
			print(f"\n {name}:{store_dict[name]}")
	
	else:
		print(f"\n Product {name} not found!")

def sell_product(store_dict, name, quantity):
	if name in store_dict:
		if quantity <= 0:
			print("\n Quantity must be greater than zero!")

		elif quantity > store_dict[name]["quantity"]:
			print("\n Not Enough Quantity in the Stock!")
			print(f"\n {name}: {store_dict[name]}")

		else:
			store_dict[name]['quantity'] -= quantity
			print(f"\n Product Name: {name}, Quantity Sold: {quantity}")
			print(f"\n SUMMARY OF TOTAL SALES")
			price = store_dict[name]["price"]
			price *= quantity
			print(f"\n Number of Product Sold: {quantity}, Total Price: {price}")
			
	else:
		print(f"\n Product {name} not Found!")


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
		total_price = store_dict[sales]["price"] * store_dict[sales]["quantity"]
		total_value += total_price
		print(f"REMAINING STOCK FOR: {sales}:{store_dict[sales]}")
	print(f"\n TOTAL VALUE OF REMAINING STOCK: {total_value}")
	

# FUNCTION TO TERMINATE PROGRAM
def terminate_program():
	print("\n Terminating Program. Goodbye! \v")
	exit()

start_program()

