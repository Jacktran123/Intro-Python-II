class Item:
    def __init__(self,name,description,pick_up=False):
        self.name=name
        self.description=description
        self.pick_up=pick_up
    def is_taken(self,item):
        if self.pick_up==True:
            print(f'You have picked up {item.name}')
        else:
            print(f'You have dropped {item.name}')
    

    