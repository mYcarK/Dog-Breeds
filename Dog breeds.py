class dog:
    
    breed="Dachshund"
    breed="Samoyed"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
Stan=dog("Dachshund","brown")
Jade=dog("Samoyed", "white")

print("Stan is a {}". format(Stan.breed))
print("Jade ia also a {}". format(Jade.breed))

print("{} is {} ".format(Stan. breed, Stan.color ))

print("{} is {} ".format(Jade. breed, Jade.color ))