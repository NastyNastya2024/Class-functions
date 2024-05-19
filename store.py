class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Item '{item_name}' added successfully.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Item '{item_name}' removed successfully.")
        else:
            print("Item not found.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Price for item '{item_name}' updated successfully.")
        else:
            print("Item not found.")

# Создание объектов магазинов
store1 = Store("SuperMart", "123 Main Street")
store1.add_item("Apples", 0.5)
store1.add_item("Bananas", 0.75)

store2 = Store("MegaStore", "456 Elm Street")
store2.add_item("Milk", 1.0)
store2.add_item("Bread", 1.5)

store3 = Store("FreshMarket", "789 Oak Street")
store3.add_item("Oranges", 0.8)
store3.add_item("Grapes", 1.2)

# Тестирование методов магазина
store1.add_item("Pears", 0.6)
print(store1.get_price("Apples"))
store1.update_price("Bananas", 0.8)
store1.remove_item("Apples")