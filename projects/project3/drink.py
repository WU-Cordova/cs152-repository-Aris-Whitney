class Drink:
    def __init__(self, name:str, price:float, size: str="Medium"): #Size default is medium, only available option
        self.name=name
        self.price=price
        self.size=size

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}" #Displays the name of the drink anf the corresponding price