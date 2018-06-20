#Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.
class movi:
    def __init__(self,name,artist,year,rating):
        self.name=name
        self.artist=artist
        self.year=year
        self.rating=rating
    def display(self):
        print("movie : %s\n artist : %s\n year : %s\n rating : %s"\
              % (self.name,self.artist,self.year,self.rating))
    def update(self):
        n = input("enter movie name : ")
        a = input("enter movie artist : ")
        y = input("enter movie year : ")
        r = input("enter movie rating : ")
        self.name = n
        self.artist = a
        self.year = y
        self.rating = r

n=input("enter movie name : ")
a=input("enter movie artist : ")
y=input("enter movie year : ")
r=input("enter movie rating : ")
m=movi(n,a,y,r)
m.display()
m.update()
m.display()