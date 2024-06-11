import pytest
from project import get_body_weight, get_body_fat_percentage, get_activity_level, calculate_maintenance_calories, calculate_macros, format_number

def test_get_body_weight():
    assert get_body_weight("150") == 150
    assert get_body_weight("200") == 200
    assert get_body_weight("250") == 250

def test_get_body_fat_percentage():
    assert get_body_fat_percentage("1") == 1
    assert get_body_fat_percentage("2") == 2
    assert get_body_fat_percentage("3") == 3

def test_get_activity_level():
    assert get_activity_level("1") == 14
    assert get_activity_level("2") == 14.5
    assert get_activity_level("3") == 15
    assert get_activity_level("4") == 15.5

def test_calculate_maintenance_calories():
    assert calculate_maintenance_calories(150, 14) == 2100
    assert calculate_maintenance_calories(150, 15) == 2250

def test_calculate_macros():
    bw = 150
    bf_level = 2
    target_calories = 1900

    # Testing with a preference for fats
    protein_grams, fat_grams, carb_grams, protein_calories, fat_calories, carb_calories = calculate_macros(bw, bf_level, target_calories, "1")
    assert protein_grams == 150
    assert fat_grams == 60
    assert protein_calories == 600
    assert fat_calories == 540
    assert carb_grams == 190
    assert carb_calories == 760

    # Testing with a preference for carbs
    protein_grams, fat_grams, carb_grams, protein_calories, fat_calories, carb_calories = calculate_macros(bw, bf_level, target_calories, "2")
    assert protein_grams == 150
    assert fat_grams == 45
    assert protein_calories == 600
    assert fat_calories == 405
    assert carb_grams == 223.75
    assert carb_calories == 895

def test_format_number():
    assert format_number(1500) == '1,500'
    assert format_number(1500.5) == '1,500.5'
    assert format_number(1500000) == '1,500,000'
    assert format_number(1500000.75) == '1,500,000.8'

