available_toppings = ['mushrooms','green peppers','olives','pepperoni','pineapple',"extrachease"]

requested_toppings1 = ['mushrooms','green peppers',"extrachease"]

if requested_toppings1:
    for requested_topping in requested_toppings1:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers right now")
        else:
            print(f"Adding {requested_topping}")
    print("\nFineshed making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

requested_topping2= []

if requested_topping2:
    for resquested_toppings in requested_topping2:
        print(f'Adding {requested_topping}')
else:
    print('Are you sure want a plain pizza?')

requested_toppings3 = ['mushrooms','french fries', 'extrachease']

if requested_toppings3:
    for requested_topping in requested_toppings3 :
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print("\nFineshed making your pizza!")
        
else:
    print('Are you sure want a plain pizza?')
