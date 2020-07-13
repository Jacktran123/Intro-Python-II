# Write a class to hold player information, e.g. what room they are in
# currently.



class Player:
    def __init__(self,name,location,items=[]):
        self.name=name
        self.location=location
        self.items=items
    def change_location(self,direction):
        if direction =='w':
            self.location=self.location.n_to
        elif direction=='s':
            self.location=self.location.s_to
        elif direction=='a':
            self.location=self.location.w_to
        elif direction =='d':
            self.location=self.location.e_to
    def action(self,action,item):
        self.location.take_or_drop_items(action,item)
        if action=='take':
            if not item in self.items:
                self.items.append(item)
                item.pick_up=True
                item.is_taken(item)
            else:
                print(f'You have picked up {item.name} already')
        elif action == 'drop':
            if not item in self.items:
                print(f'You don\'t have that item')
            else: 
                item.pick_up=False
                item.is_taken(item)
                self.items.remove(item)
                
    def show_items(self):
        for i in range(len(self.items)):
            print(f'You have {self.items[i].name}')    
        if len(self.items)==0:
            print('You don\'t have anything')


       