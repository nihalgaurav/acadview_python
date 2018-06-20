#Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class temprature:
    def convert_f(self,c):
        self.f=(9/5*c)+32
        print("%f celcius = %f farenhight " % (c,self.f))
    def convert_c(self,f):
        self.c=5/9*(f-32)
        print("%f ferenhight = %f celcius"%(f,self.c))

t=temprature()
c=float(input("enter in celcius to convert in farenhight :"))
t.convert_f(c)
f=float(input("enter in farenhight to convert in celcius :"))
t.convert_c(f)
