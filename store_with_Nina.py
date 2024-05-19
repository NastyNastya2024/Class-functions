class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print (f'Item {item_name} has been added to {self.name} ')

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print (f'Item {item_name} has been removed from {self.name} ')

    def get_price (self,item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print (f'Item {item_name} has been updated to {new_price} ')
        else:
            print (f'Item {item_name} does not exist')


store1 = Store('Nina Store', '123 Main Street')
store2 = Store('Store', '12  Street')
store3 = Store('Nina ', '13 Main Street')

store1.add_item('bread', 100)
store1.add_item('milk', 100)
store2.add_item('milk', 200)
store3.add_item('eggs', 300)

print(store1.items)
store1.remove_item('bread')
store1.get_price('milk')
print(store1.get_price('milk'))

store1.update_price('milk', 200)




