

class Fruit:
    def __init__(self,m,r):
        print("Hey i am a fruit")
        self.name=m
        self.season=r

    def info(self):
        print(f"{self.name} is avilable in {self.season}")

a=Fruit("Mango" , "Summer")
a.info()
b=Fruit("Apple" , "Winter")
b.info()