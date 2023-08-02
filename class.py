class car:
    doors = 4
    off=True
#if the funtion is called with _ we dont have to change it outside the clasz
    def on(self):
        self.off = False
    #the self. is for referer to the functionon the class

lambo = car()
lambo.on()  

print(lambo.doors)

class static:
    number = 1

    def addition():
        static.number +=1

static.addition()
print(static.number)

