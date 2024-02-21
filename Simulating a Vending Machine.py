inventory = {
   "Cola":  {"price": 1.50,  "quantity": 5}, 
   "Candy": {"price": 0.75,  "quantity": 2},
   "Chips": {"price": 1.00,  "quantity": 3},
   "Soda":  {"price": 1.25,  "quantity": 4},
   "Water": {"price": 1.00,  "quantity": 1},
   "Gum":   {"price": 0.50,  "quantity": 2},
   "Cookie": {"price": 1.00,  "quantity": 1},
   "Cake":  {"price": 3.00,  "quantity": 1},
   "Bread": {"price": 2.00,  "quantity": 1},
   "Milk":  {"price": 2.50,  "quantity": 1},
   "Eggs":  {"price": 3.00,  "quantity": 1},
  "Butter": {"price": 1.00,  "quantity": 1},
  "Jam": {"price": 1.00,  "quantity": 1},
  "Cheese": {"price": 1.00,  "quantity": 1},
  "Yogurt": {"price": 1.00,  "quantity": 1},
  "Honey": {"price": 1.00,  "quantity": 1},
  "Baking Soda": {"price": 1.00,  "quantity": 1},
  "Baking Powder": {"price": 1.00,  "quantity": 1},
  "Sugar": {"price": 1.00,  "quantity": 1},
  "Flour": {"price": 1.00,  "quantity": 1},
  "Chocolate": {"price": 1.00,  "quantity": 1},
  "Vanilla": {"price": 1.00,  "quantity": 1},
  "Strawberry": {"price": 1.00,  "quantity": 1},
  "Blueberry": {"price": 1.00,  "quantity": 1},
  "Raspberry": {"price": 1.00,  "quantity": 1},
  "Blackberry": {"price": 1.00,  "quantity": 1},
  "Mango": {"price": 1.00,  "quantity": 1},
  "Pineapple": {"price": 1.00,  "quantity": 1},
  "Apple": {"price": 1.00,  "quantity": 1},
  "Orange": {"price": 1.00,  "quantity": 1},
  "Grape": {"price": 1.00,  "quantity": 1},
  "Peach": {"price": 1.00,  "quantity": 1},
  "Plum": {"price": 1.00,  "quantity": 1},
  "Apricot": {"price": 1.00,  "quantity": 1},
  "Lemon": {"price": 1.00,  "quantity": 1},
  "Lime": {"price": 1.00,  "quantity": 1},
  "Kiwi": {"price": 1.00,  "quantity": 1},
  "Pear": {"price": 1.00,  "quantity": 1},
  "Cherry": {"price": 1.00,  "quantity": 1},
  "Melon": {"price": 1.00,  "quantity": 1},
  "Papaya": {"price": 1.00,  "quantity": 1},
  "Pomegranate": {"price": 1.00,  "quantity": 1},
  "Grapefruit": {"price": 1.00,  "quantity": 1},
  "Passionfruit": {"price": 1.00,  "quantity": 1},
  "Watermelon": {"price": 1.00,  "quantity": 1},
  "Honeydew": {"price": 1.00,  "quantity": 1},
  "Cantaloupe": {"price": 1.00,  "quantity": 1},
   # ... more items
}
# Function to display the inventory
def display_inventory():
    print("inventory:")
    for item, details in inventory.items():
        print(f"{item}: ${details['price']} ({details['quantity']} available)")
        if details['quantity'] == 0:
         print(f"{item}: ${details['price']} (Out of stock)")

select_item = input("Enter the item you want to purchase: ")
# Check if the item exists in the inventory
if select_item in inventory and inventory[select_item]['quantity'] > 0:
    print(f"Item: {select_item}")
    print(f"Price: ${inventory[select_item]['price']}")
    insert_money = float(input("insert money: "))
    if insert_money >= inventory[select_item]['price']:
        inventory[select_item]['quantity'] -= 1
        print(f"Thank you for your purchase of {select_item}!")
    else:
        print("Insufficient funds. Please insert more money.")
