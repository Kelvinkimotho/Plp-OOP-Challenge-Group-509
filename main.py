from pet import Pet

# We create a pet Object
my_pet = Pet("Max")
print(f"Creating pet: {my_pet.name}")

# Interacting the pet
my_pet.eat()
#my_pet.play()
#my_pet.sleep()
my_pet.train("roll over")
#my_pet.train("play dead")

# Checking status
my_pet.get_status()
