class books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f'{self.title} by {self.author}, {self.pages} pages.'
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author and self.pages == value.pages
    
    def __lt__(self, value):
        return self.pages < value.pages
    
    def __gt__(self, value):
        return self.pages > value.pages
    
    def __add__(self,value):
        return self.pages + value.pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author or keyword in self.pages
    
    def __getitem__(self,key):
        if key=='title':
            return self.title
        elif key=='author':
            return self.author
        elif key=='pages':
            return self.pages
        else:
            return "Invalid key"



book1=books("Atomic Habits","James Clear",338)
book2=books("The 7 Habits of Highly Effective People","Stephen Covey",416)
book3=books("The 10X Rule","Grant Cardone",272)
 

print(book1)
print(book1==book1)
print(book1<book2)
print(book1>book3)
print(book1+book2)
print("Atomic" in book1)
print(book1["title"])