class trip:
    name=""
    drink=""
    food=""
    smoke=""
    
    def party(self):
        print("Lets Party!!")

bavan = trip()
priyan = trip()

bavan.name= input()
bavan.drink="Thumbs Up"
bavan.food="Pizza"
bavan.smoke="No"

priyan.name="Priyan"
priyan.drink="Beer"
priyan.food="Burger"
priyan.smoke="Yes"

print("TICKET NO1- Name:",bavan.name+", Drink:",bavan.drink+", Food:",bavan.food+", Smoke:",bavan.smoke)
print("TICKET NO2- Name:",priyan.name+", Drink:",priyan.drink+", Food:",priyan.food+", Smoke:",priyan.smoke)

bavan.party()