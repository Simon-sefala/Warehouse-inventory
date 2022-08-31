# Create a class named Shoes with the following attributes 
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This function returns the cost of the shoe    
    def get_cost(self):
        self.cost = shoes_objects[3]


    # This function returns the quantity of the shoe  
    def get_quantity(self):
        self.quantity = shoes_objects[4]


    # This function lets a user add stock to a product
    def set_quantity(self, quantity):
        self.quantity += quantity


    # This method returns a string representation of a class
    def __str__(self):
        output = f"Country:  {self.country}\n"\
                 f"Code:     {self.code}\n"\
                 f"Product:  {self.product}\n"\
                 f"Cost:     {self.cost}\n"\
                 f"Quantity: {self.quantity}\n"
        return output


# A variable with an empty list
shoes_objects = [] 


# This function reads from a text file called inventory.txt and appends that data into the list shoes_objects
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            file_contents = file.readlines()
            for line in file_contents[1:]:
                line = line.strip('\n').split(",")
                line_invetory = Shoes(line[0], line[1], line[2], float(line[3]), int(line[4]))
                shoes_objects.append(line_invetory)
    except FileNotFoundError:
        print("The file does not exist")


# This function lets the user to capture a new object into the list
def capture_shoes():
    Country = input("Enter country: ")
    Code = input("Enter the SKU code: ")
    product = input("Enter the name of the product: ")
    cost = float(input("Enter the cost of the product: "))
    quantity = int(input("Enter the quatity of the product: "))
    new_inventory = Shoes(Country, Code, product, cost, quantity)
    shoes_objects.append(new_inventory)


# This function lets the user view all the items in the inventory
def view_all():
    for s in shoes_objects:
        print(s)


# This function lets the user add stock to a product with low stock
def restock():
    low_stock = shoes_objects[0]
    for shoe_obj in shoes_objects:
        if shoe_obj.quantity <= low_stock.quantity:
            low_stock = shoe_obj
    print(low_stock)
    update = input("Would you like to add new stock? yes/no?: ")
    if update == "yes":
        how_much = int(input("How much stock would you like to add: "))
        low_stock.set_quantity(how_much)
        print(low_stock)
    elif update == "no":
        exit()
    else:
        print("Invalid choice")


# This function lets a user search for a product in the inventory
def search_shoe():
    
    found = False
    shoe_search = input("Which shoe would you likme to search for?: ")
    for shoe_obj in shoes_objects:
        if shoe_obj.product == shoe_search:
            print(shoe_obj)
            found = True 
            break
    if not found:
        print("Shoe not found in inventory")


# This function returns the total stock value of each product in the inventory
def value_per_item():
    for item in shoes_objects:
        value = item.cost * item.quantity
        print(f'Product name: {item.product}\n'
              f'Value of product: R{value}\n')


# This function returns the product with the highest quantity in the inventory
def highest_qty():
    high_stock = shoes_objects[0]
    for shoe_obj in shoes_objects:
        if shoe_obj.quantity >= high_stock.quantity:
            high_stock = shoe_obj
    print(f'Product: {high_stock}\n'
          f'This item is for sale')
        

# According to the input from the user the relevent function will be called and perform such operation
while True:
    # This menu will ask the user which operation  they would like to perform
    menu = input('''What would you like to do?:
ds- displays all inventory
as- add a new product
rs- restock product
s- search for a product
gv- get value of each item
hq- view product with highest quatity
e- exit:
''').lower()
    if menu == "ds":
        read_shoes_data()
        view_all()
    elif menu == "as":
        read_shoes_data()
        capture_shoes()
    elif menu == "rs":
        read_shoes_data()
        restock()
    elif menu == "s":
        read_shoes_data()
        search_shoe()
    elif menu == "gv":
        read_shoes_data()
        value_per_item()
    elif menu == "hq":
        read_shoes_data()
        highest_qty()
    elif menu == "e":
        print("Goodbye!!!")
        exit()
    else:
        print("Invalid choice")
        menu = input('''What would you like to do?:
ds- displays all inventory
as- add a new product
rs- restock product
s- search for a product
gv- get value of each item
hq- view product with highest quatity
e- exit:
''').lower()
