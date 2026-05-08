def apply_discount(category_type: str, amount: float):
    """
    Calculate discount based on category.    
    """
    category = {
        "student": .2,
        "pwd": .25,
        "senior": .25,
        "regular": 0,
    }

    final_amount = amount - (category[category_type] * amount)

    return final_amount

buy_car = input("do you wanna buy a car [Y/N]: ").capitalize()

if buy_car == "Y":
    print(cars)
    what_car = input("what car do you wanna buy? ").capitalize()
    car_variant = cars[what_car]
    print(car_variant)
    sure = input("are you sure you wanna buy? [Y/N]: ").lower()
    if sure == "y":
        customer_category = input("""Customer categories
              [pwd] Persons with Disability
              [regular] Regular
              [student] Student
              [senior] Senior Citizen
              """).lower()
        car_amount = float(car_variant.get("amount"))
        car_total_amount = apply_discount(customer_category, car_amount)
        print(f"Total car price with {customer_category.capitalize()} discount {car_total_amount}")
        amount = float(input("Please input amount: "))
        
        if amount >= car_total_amount:
            print(f"Your change is {amount - car_total_amount}")
        else:
            print("Insufficient Balance")
        
    else:
        print("Thank you for visiting us.")
else:
    print("Thank you for visiting us.")