def greet_user(username):
    print(f"Hello {username}")

greet_user("Nouman")


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')


# *********************

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

# Calling the functions with a copy of the list to preserve the original list
# This way, the original list remains unchanged for further use.
# print_models(unprinted_designs[:],completed_models
# )

show_completed_models(completed_models)