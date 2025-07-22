class dog:
    
    breed="Dachshund"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
Stan=dog("Dachshund",10)
Jade=dog("Dachshund",15)

print("Stan is a {}". format(Stan.breed))
print("Jade ia also a {}". format(Jade.breed))

print("{} is {} years old".format(Stan. breed, Stan.color ))

print("{} is {} years old".format(Jade. breed, Jade.color ))