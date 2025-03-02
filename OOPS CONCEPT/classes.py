class Person:
    name="satish"
    job="SDE"
    salary=90000

    def info(self):
        print(f"{self.name} is a {self.job}")

a= Person()      #creating objects
print(a.name , a.job , a.salary )

a.info( )  #information of object a