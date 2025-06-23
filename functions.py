def greet_user(username):
    print(f"Hello {username}")

greet_user("Nouman")


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')