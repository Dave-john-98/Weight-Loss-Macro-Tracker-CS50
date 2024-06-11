def main():
    print("===============================================")
    print("Macro Tracker for Weight Loss")
    print("Your Name: Dave John")
    print("GitHub Username: Dave-John-98")
    print("edX Username: davej98")
    print("City and Country: New York, NY USA")
    print("Date: 6-Jun-2024")
    print("===============================================\n")

    print(f"\nWelcome to the Macro Tracker for Weight Loss")

    bw = (input(f"\nEnter your body weight (in lbs): "))
    body_weight = float(get_body_weight(bw))

    print(f"\nSelect your body fat level:")
    print(f"\n1. Excess Body Fat")
    print("""
    Male: Above 25%
    Female: Above 32%
    Description: Significant amount of visible fat, lack of muscle definition.
    """)
    print("2. In Shape")
    print("""
    Male: 15-20%
    Female: 25-30%
    Description: Moderate amount of visible fat, some muscle definition.
    """)
    print("3. Competitive")
    print("""
    Male: 6-12%
    Female: 15-20%
    Description: Low body fat, high muscle definition, often seen in athletes.
    """)
    print("Here is a link to an reference chart for you to choose what level you think best applies to you")
    print(f"\nURL: https://i.pinimg.com/736x/86/06/9c/86069c2b664db5c7b11056cbb30a457d.jpg")

    bf_level = input(f"\nEnter the number corresponding to your body fat level (1-3): ")
    bf = get_body_fat_percentage(bf_level)

    print(f"\nSelect your activity level:")
    print("1. Sedentary")
    print("2. Lightly active")
    print("3. Moderately active")
    print("4. Very active")

    activity_level = input(f"\nEnter the number corresponding to your activity level(1-4): ")
    activity = get_activity_level(activity_level)

    maintenance_calories = calculate_maintenance_calories(body_weight, activity)
    print(f"\nYour Maintenance Calories would be {format_number(maintenance_calories)}")

    target_calories = maintenance_calories - 500
    print(f"""\nFor a healthy calorie deficit for weight loss, we should aim for about
500 calories deficit which would be {format_number(target_calories)} based on your body weight.""")

    print(f"\nDo you prefer a diet higher in fats or carbs?")
    print("1. Higher in fats (nuts, seeds, almonds, etc.)")
    print("2. Higher in carbs (rice, pasta, bread, etc.)")

    preference = input(f"\nEnter the number corresponding to your preference (1 or 2): ")
    protein_grams, fat_grams, carb_grams, protein_calories, fat_calories, carb_calories = calculate_macros(body_weight, bf, target_calories, preference)

    print(f"\nHere are your Nurtition Goals:")
    print(f"\nYour target daily intake: {format_number(target_calories)} Calories")
    print(f"Protein: {format_number(protein_grams)}g / {format_number(protein_calories)} Calories")
    print(f"Fats: {format_number(fat_grams)}g / {format_number(fat_calories)} Calories")
    print(f"Carbs: {format_number(carb_grams)}g / {format_number(carb_calories)} Calories")

def get_body_weight(x):
    while True:
        try:
            x = float(x)
            if x > 0:
                return x
            elif x == 0:
                print(f"\nInvalid Input: Body weight cannot be 0")
                x = input(f"\nEnter your body weight (in lbs): ")
                pass
            else:
                print(f"\nInvalid Input: Body weight cannot be negative")
                x = input(f"\nEnter your body weight (in lbs): ")
                pass
        except (ValueError,TypeError):
            print(f"\nInvalid Input: Not a number")
            x = input(f"\nEnter your body weight (in lbs): ")

def get_body_fat_percentage(bf_level):
    while True:
        try:
            bf_level = int(bf_level)
            if bf_level in [1,2,3]:
                return bf_level
            else:
                print(f"\nInvalid Input: Pick a level between 1, 2, or 3")
                bf_level = input(f"\nEnter the number corresponding to your body fat level (1-3): ")
                pass
        except(ValueError,TypeError):
            print(f"\nInvalid Input: Pick a level between 1, 2, or 3")
            bf_level = input(f"\nEnter the number corresponding to your body fat level (1-3): ")

def get_activity_level(activity_level):

    while True:
        try:
            activity_level = int(activity_level)
            activity_values = [14, 14.5, 15, 15.5]
            if activity_level in [1,2,3,4]:
                return activity_values[activity_level - 1]
            else:
                print(f"\nInvalid Input: Pick a level between 1, 2, 3, or 4")
                activity_level = input(f"\nEnter the number corresponding to your activity level(1-4): ")
                pass
        except (ValueError,IndexError):
            print(f"\nInvalid Input: Pick a level between 1, 2, 3, or 4")
            activity_level = input(f"\nEnter the number corresponding to your activity level(1-4): ")

def calculate_maintenance_calories(bw, activity_level):
    return bw * activity_level

def calculate_macros(bw, bf_level, target_calories,preference):
    protein_constants = {1: 0.75, 2: 1.0, 3: 1.25}
    protein_grams = bw * protein_constants[bf_level]

    while True:
        try:
            preference = int(preference)
            if preference in [1,2]:
                if preference == 1:
                    fat_preference = 0.4
                    break
                elif preference == 2:
                    fat_preference = 0.3
                    break
            else:
                print(f"\nInvalid Input: Pick 1 or 2")
                preference = input(f"\nEnter the number corresponding to your preference (1 or 2): ")
                pass
        except (ValueError):
            print(f"\nInvalid Input: Pick 1 or 2")
            preference = input(f"\nEnter the number corresponding to your preference (1 or 2): ")

    fat_grams = bw * fat_preference

    protein_calories = protein_grams * 4
    fat_calories = fat_grams * 9

    carb_calories = target_calories - (protein_calories + fat_calories)
    carb_grams = carb_calories / 4

    return protein_grams, fat_grams, carb_grams, protein_calories, fat_calories, carb_calories

def format_number(value):
    return f"{value:,.0f}" if value.is_integer() else f"{value:,.1f}"

if __name__ == "__main__":
    main()
