class Menu:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'{item_name} Removed Successfully')
        else:
            print(f'{item_name} Not Found')
    
    def view_menu(self):
        print("----------------Menu Information----------------")
        print(f' Name       Price       Quantity')
        for item in self.items:
            print(f'{item.name}       {item.price}           {item.quntity}')
        print("----------------------------------------------------")


# Menu Item Class
# kf