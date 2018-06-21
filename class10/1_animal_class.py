#Create a class Animal as a base class and define method animal_attribute. Create another \
# class Tiger which is inheriting Animal and access the base class method.
class animal:
    def animal_attribute(self):
        print("animal speaks")
        print("animal eats")
class tiger(animal):
    pass
t1=tiger()
t1.animal_attribute()
t1.tiger_attributes()