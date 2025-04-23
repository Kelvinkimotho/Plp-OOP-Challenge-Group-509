from pet import Pet

# We create a pet Object
# my_pet = Pet("Max")
# print(f"Creating pet: {my_pet.name}")

#ask user for pet name
name = input("Enter your pet's(cat) name: ")
my_pet = Pet(name)
# Interacting the pet
my_pet.eat()
my_pet.play()
my_pet.sleep()
print(f"\n{name}: Has been trained on the following tricks..")
my_pet.train("roll over")
my_pet.train("play dead")
your_train = input("\nEnter additional trick your pet is trained: ")
my_pet.train(your_train)

# Checking status
my_pet.get_status()

# Creating another pet object
print("\nCreating pet: Cat")
my_pet2 = Pet("Cat", "cat")

# Interaction.
my_pet2.speak()
my_pet2.wake_up()
my_pet2.get_status()
