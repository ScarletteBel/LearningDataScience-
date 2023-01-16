# working with inheritance in Python
class ShoeFactory:

    def __init__(self, skind, scode):
        self.shoetype = skind
        self.shoecode = scode

    def description(self):
        return (self.shoetype + " : " + self.shoecode)


class Shoe(ShoeFactory):
    def __init__(self, kind, code, color):
        ShoeFactory.__init__(self, kind, code)
        self.shoecolor = color

    def description(self):
        return (self.shoetype + " : " + self.shoecode + ' ' + self.shoecolor)


x = ShoeFactory("boots", "111111")
y = Shoe("sport", "555555", "brown")

print(x.description())
#print(y.getShoe())
print(y.description())
