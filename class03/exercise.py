#create a class of Fruit
    #give it 3 attributes (1 shoudl be price)
    #define 3 methods that access the atributes and return them
    #define a method that changes the price to a new price (taken as an parameter)
        #and return a new price
        
class Fruit:
    def __init__(self, name, price, origin, freshness):
        self.price = price
        self.name = name
        self.origin = origin
        self.freshness = freshness
    
    def get_price(self):
        return self.price
    
    def get_origin(self):
        return self.origin
    
    def get_freshness(self):
        return self.freshness

    def get_discounted_price(self):
        if self.freshness<10: 
            return self.price * 0.8
        else:
            return self.price
    
    def set_price(self, new_price):
        self.price = new_price
        print(f"New price is set to {new_price}!")
    
    
fruit1 = Fruit("apple", 10, "canada", 9)
fruit2 = Fruit("Durian", 20, "vietnam",10)
fruit3= Fruit("organe", 5, "california",10)
print(fruit1.name)
print(fruit1.get_discounted_price())
print(fruit1.set_price(7))

fruits = [fruit1, fruit2, fruit3]
for fruit in fruits:
    print(f"{fruit.name} is ${fruit.price} from {fruit.origin} with the freshness of {fruit.freshness}")