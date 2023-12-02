age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age_wks = float(age) * 52

limit_age = 90
limit_age_wks = float(limit_age) * 52


final_age = limit_age_wks - age_wks

print(f"You have {int(final_age)} weeks left.")
