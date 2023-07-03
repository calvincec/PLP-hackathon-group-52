print("Based on your input, we want to calculate the number of calories you have consumed in a day: ")
fat_grams = int(input("Enter the number of grams of fat: "))
carb_grams = int(input("Enter the number of grams of carbohydrates: "))
fat_grams *= 9
carb_grams *= 4
total_calory = fat_grams + carb_grams
print("Calories from the fats is" ,fat_grams, "while from carbohydrates is ",carb_grams)
print("Total calories in your body will therefore be ",total_calory)