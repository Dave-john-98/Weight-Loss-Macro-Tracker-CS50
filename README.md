# Macro Tracker for Weight Loss

#### Video Demo: [Macro Tracker Demo](<https://youtu.be/vcCKz8eDeGg>)

## Introduction
This project is a Macro Tracker designed to help users track their macronutrient intake for weight loss. It calculates daily calorie needs based on body weight, body fat percentage, and activity level. It then provides macronutrient goals in terms of proteins, fats, and carbohydrates.

## Features
1. **Calculates Maintenance Calories**: The program calculates the daily maintenance calories based on the user's body weight and activity level.
2. **Calorie Deficit for Weight Loss**: It adjusts the maintenance calories to create a calorie deficit suitable for weight loss.
3. **Macronutrient Goals**: The program provides daily macronutrient goals in grams and calories, tailored to the user's dietary preferences.

## Demonstration
The project guides the user through a series of inputs to gather necessary information for calculating macronutrient goals. Here is a step-by-step breakdown of how the program works:

1. **User Input for Body Weight**: The user is prompted to enter their body weight in pounds.
2. **User Input for Body Fat Percentage**: The user selects their body fat percentage level from three options: Excess Body Fat, In Shape, and Competitive.
3. **User Input for Activity Level**: The user selects their activity level from four options: Sedentary, Lightly Active, Moderately Active, and Very Active.
4. **Calculate Maintenance Calories**: Based on the inputs, the program calculates the maintenance calories.
5. **Calorie Deficit Calculation**: The program creates a calorie deficit of 500 calories for weight loss.
6. **User Dietary Preference**: The user selects their dietary preference, whether they prefer a higher fat diet or a higher carb diet.
7. **Macronutrient Calculation**: The program calculates the grams and calories for proteins, fats, and carbohydrates based on the user's dietary preference.
8. **Output**: The program outputs the daily caloric intake and the distribution of macronutrients in grams and calories.

## Files in the Project
### `project.py`
- **Purpose**: The main script that runs the Macro Tracker program.
- **Functions**:
  - `main()`: Orchestrates the flow of the program, prompting user inputs and displaying results.
  - `get_body_weight(x)`: Prompts the user to input their body weight and validates the input.
  - `get_body_fat_percentage(bf_level)`: Prompts the user to select their body fat percentage level and validates the input.
  - `get_activity_level(activity_level)`: Prompts the user to select their activity level and validates the input.
  - `calculate_maintenance_calories(bw, activity_level)`: Calculates maintenance calories based on body weight and activity level.
  - `calculate_macros(bw, bf_level, target_calories, preference)`: Calculates the macronutrient distribution based on user inputs.
  - `format_number(value)`: Formats numbers for display, adding commas as needed.

### `test_project.py`
- **Purpose**: Contains test cases for the functions in `project.py` to ensure they work as expected.
- **Functions**:
  - `test_get_body_weight()`: Tests the `get_body_weight` function with various inputs.
  - `test_get_body_fat_percentage()`: Tests the `get_body_fat_percentage` function with various inputs.
  - `test_get_activity_level()`: Tests the `get_activity_level` function with various inputs.
  - `test_calculate_maintenance_calories()`: Tests the `calculate_maintenance_calories` function with predefined inputs and expected outputs.
  - `test_calculate_macros()`: Tests the `calculate_macros` function with different user preferences for fats and carbs.
  - `test_format_number()`: Tests the `format_number` function to ensure correct number formatting.


### Design Choices
When designing this project, several choices were made to enhance user experience and ensure accurate calculations:
1. **User Prompts**: Clear and informative prompts guide the user through each step, ensuring they provide the necessary information.
2. **Input Validation**: Each input is validated to ensure it meets the expected criteria, with re-prompts for invalid inputs.
3. **Calorie Deficit**: A standard calorie deficit of 500 calories was chosen for weight loss, balancing effectiveness and safety.
4. **Dietary Preferences**: Users can choose between a higher fat or higher carb diet, making the tracker flexible and accommodating different dietary needs.

## Conclusion
This Macro Tracker project helps individuals manage their diet effectively for weight loss by providing precise macronutrient goals. It simplifies the process of calculating daily caloric intake and macronutrient distribution, making it easier for users to follow a weight loss plan. Thank you for exploring my project!
