# Let's create a Product from different formats

# you're designing a product class
    # product class needs:
        # name
        # price
        # category
        
# the data to create this class may arrive in 3 different formatss:
    # 1. seperate constructor agrument( __init__)
    # 2. one comma-seperated string
    # 3. a dictionary
    
# you need to design the class so all three formats can be used cleanly

# example of the dictionary:
example_dict = {
    "name" : "something",
    "price": 0,
    "category": "something else"    
}

# example of comma seperated
ex_str = "something, 0, something else"
# hint --> int(str) convert a stirng to integer

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    @classmethod
    def from_string(cls, str):
        name, price, category = str.split(",")
        return cls(name, float(price), category)
    
    @classmethod
    def from_dict(cls, dict):
        name = dict["name"]
        price = float(dict["price"])
        category = dict["category"]
        return cls(name, price, category)
    
    @classmethod
    def new_product(cls, name):
        return cls(name,0, "")
    
    def display(self):
        print(f" {self.name} - {self.price} - {self.category}")
    
p1 = Product.from_dict(example_dict)
p2 = Product.from_string(ex_str)
p3 = Product.new_product("newproduct")
p1.display()
p2.display()
p3.display()