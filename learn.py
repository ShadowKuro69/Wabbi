bot_name = "Wabbi"
user_name = "kuro"
hours_coded = 11
add_hours = 2

print(bot_name)
print(user_name)
print(hours_coded)
print(add_hours)

def greet_user(name):
    print("yoooo " + name + ", welcome to wabbi!")
def addition(hours):
    print("yours hours are " + str(hours) + str(hours_coded) + ", Good work")

greet_user(user_name)
addition(add_hours)




if hours_coded > 10:
    print("Youre on fire!")
else:
    print("slacker....")


user_profile = {
        "name": "kuro",
        "hours": 0,
        "wins": 0,
        "losses": 0
}

user_profile["wins"] = 3
print(user_profile["wins"])
    
print(user_profile["name"])
print(user_profile["wins"])