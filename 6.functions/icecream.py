def make_icecream(flavor,*toppings):
    """Print the ice cream order details."""
    print(f"\nMaking a {flavor} ice cream with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")