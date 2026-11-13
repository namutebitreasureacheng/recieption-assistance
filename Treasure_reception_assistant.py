def get_meals(meal,cost):
    if 'meal' == 'Snack Box' and 'cost'== 3000:
        return True
    elif 'meal' == 'Meal Plate' and 'cost' == 8000:
        return True
    elif 'meal' == 'Combo Meal' and 'cost' == 12000:
        return 'True'
    else:
        return None



def safe_int(prompt):
    while True:
        try:
            number=int(input(prompt))
            return number
        except ValueError:
            print("Invalid Input")

def calculate_total(snack, meal, combo):
    subtotal = (snack* 3000) + (meal*8000) + (combo*12000)
    return(subtotal)

menu=[]
count_snack = 0
count_Meal = 0
count_Combo = 0
total=0
subtotal = 0


print("Welcome to the UCU Canteen!")
hour = safe_int("Enter current hour (0-23): ")
if hour < 0 or hour > 23:
    print("The hours are from 0 to 23.")
elif hour < 7 or hour > 20:
    print("Sorry, Canteen is closed. It opens from 7 to 20.")
else:
    print("Menu:")
    print('1. Snack Box - UGX 3000')
    print('2. Meal Plate' - 'UGX 8000')
    print('3. Combo Meal' - 'UGX 12000')



snack = safe_int("Enter number of Snack Boxes: ")
meal = safe_int("Enter number of Meal Plate: ")
combo = safe_int("Enter number of Combo Plate: ")

student_id = safe_int("Enter your 7-digit Student: ")
if len(student_id) != 7:
    print("Numbers are lessthan 7.")
else:
    count_Snack =snack
    count_Meal =meal
    count_Combo =combo
    total = count_Snack + count_Meal + count_Combo

subtotal = calculate_total(snack, meal, combo)
if subtotal > 40000:
    discount = subtotal * 0.10
else:
    discount = 0

total_to_pay = subtotal - discount


print("Order Summary:")
print(f"Snack Boxes: {count_Snack}")
print(f"Meal Plates: {count_Meal}")
print(f"Combo_Meals: {count_Combo}")
print(f"Total items: {total}")
print(f"Subtotal: UGX{subtotal}")
print(f"Discount: {discount}")
print(f"Student id: {student_id}")
print(f"Total to pay: UGX {total_to_pay}")







