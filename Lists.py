# Take in user input in pairs of city names and miles from previous cities.
# When the user types "done" for the city name, prompt the user for the range of their car.
# Finally, print out the furthest city in the route that the user can make it to before recharging.

def run():
    getting_cities = True
    i = 0
    total = 0
    miles_list = []
    location_list = []
    user_range = 0
    while getting_cities:
        #print(getting_cities)
        city = input("City: ")
        if city == "done":
            getting_cities = False
        else:
            miles = int(input("Miles: "))
            miles_list.append(miles)
            location_list.append(city)
    
    while i < len(miles_list):
        total += miles_list[i]
        i += 1
        
    if getting_cities == False:
        #print(getting_cities)
        user_range = int(input("Range: "))
    for i in range(len(miles_list)):
        
        if user_range < miles_list[i] and i == 0:
            # print(user_range < miles_list[i])
            # print(i == 0)
            print("You cannot make it to your first stop.")
            return
        user_range -= miles_list[i] 
        if user_range < 0:
            print("You can make it to " + str(location_list[i - 1]) + " before recharging.")
            return
        
            
        getting_cities = False
    print("You can make it all the way to your destination.")
# print(getting_cities)


        


    






















if __name__ == "__main__":
    run()
