#Following Object Oriented Programming with Python - Full Course for Beginners https://www.youtube.com/watch?v=Ej_02ICOIgs

class  Item:

    all = []
    def __init__(self,name : str ,price  : float ,quantity=0 ):
        #Run validatons to the received arguments.

        assert price >=0,  f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0 , f"Quantity {quantity} is not greater than or equal to  zero!"


        #Asign to self object
        self.name= name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)


    def calculate_total_price(self, price, quantity):
        return price * quantity

    #everytime the item is represented like for example <__main__.Item object at 0x000001F1F5D6BEB0> , when doing print(object), it will be automatically formated to the return.
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1= Item("Phone",100,1)
item2= Item("Laptop",1000,3)
item3= Item("Cable",10,5)
item4= Item("Mouse",50,5)
item5= Item("Keyboard",75,5)

print(Item.all)