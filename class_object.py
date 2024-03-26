class Person:
    def __init__(self,name,age,gender):
        self.n=name
        self.a=age
        self.g=gender

    def introduce(self):
        print(f"Hello, My name is {self.n} and I am {self.a} years of age. I am of the {self.g} gender.")   


person_1=Person("Justin",19,"Male")
person_1.introduce()


        