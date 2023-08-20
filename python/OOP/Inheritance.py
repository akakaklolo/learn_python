class Fruit :
    def __init__(self,color,flavor):
        self.color = color
        self.flavor= flavor
class Apple(Fruit):
    pass
class Grap(Fruit):
    pass
granny_smith= Apple("Red","Tart")
Carnelian = Grap("Purple","Sweet")
print(granny_smith.flavor)
print(Carnelian.color)
####################################
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()