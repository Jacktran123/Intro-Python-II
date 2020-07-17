# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,n_to=None,s_to=None,w_to=None,e_to=None,items=None):
        self.name=name
        self.description=description
        self.n_to=n_to
        self.s_to=s_to
        self.e_to=e_to
        self.w_to=w_to
        self.items=items
    def add_items(self,item):
        self.items=[]
        self.items.append(item)
    def take_or_drop_items(self,action,item):
        if action=='take' and len(self.items)>0:
            self.items.remove(item)
        elif action=='drop':
            self.items.append(item)
    def show_items(self):
        if self.items:
            print('Here is the available items in the room')
            for i in range(len(self.items)):
                print(self.items[i].name +' -- '+self.items[i].description)
        elif not self.items:
            print('The room is currently empty.You should move on')
        elif self.items and len(self.items)==0:
            print('The room is currently empty.You should move on')
    

    

