from drink import Drink
class OrderItem:
    def __init__(self, drink: Drink, customization: str =''):
        self.drink=drink
        self.customization=customization

    def __repr__(self):
        if self.customization:
            return f"{self.drink.name} ({self.customization})" #returns the name of the drink and any customizations
        else:
            return f"{self.drink.name} (No Customization)" #If no input is added for customizations, retun No Customizations