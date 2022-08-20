print("Hello"[4])
#########################################
print(123 + 345)
#########################################
print(100/3)
########################################################
num_char = len(input("whats your name?\n"))
new_num_char = str(num_char)
print("the number of alphabets in your name are "+new_num_char)
##########################################################
res = 2**4
print(res)
############################################################
print(3*3+3/3-3) #PEMDAS
###############################################
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
height_new = float(height)
weight_new = float(weight)
bmi = weight_new/(height_new**2)
bmi_new = int(bmi)
print(bmi_new)
######################################################
print(round(8/3,4))
###################################################
print(8//3)
################################################
score = 6
score += 1
score *= 3
score -= 2
score /= 4
print(score)
##############################################
score1 = 32
float1 = 4.34
isLosing = False
print(f"The score of the person is {score1} and the float is {float1} and is he losing = {isLosing}")
#########################################################################################################
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)
z_months = years_left*12
y_weeks = years_left*52
x_days =  years_left*365

print(f"You have {x_days} days, {y_weeks} weeks, and {z_months} months left.")


Output - 
o
468
33.333333333333336
whats your name?
Priyam
the number of alphabets in your name are 6
16
7.0
enter your height in m: 1.85
enter your weight in kg: 82
23
2.6667
2
4.75
The score of the person is 32 and the float is 4.34 and is he losing = False
What is your current age?20
You have 25550 days, 3640 weeks, and 840 months left.




