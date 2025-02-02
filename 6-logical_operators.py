#or
#and
#not

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is sitll scheduled!")


temp = -5
is_sunny = False

if temp >= 28 and is_sunny:
    print("Its Hot Outside")
    print("Its Sunny")

elif temp <=0 and is_sunny:
    print("Its Cold Outside")
    print("Its Sunny")

elif 28 > temp > 0 and is_sunny:
    print("Its Warm Outside")
    print("Its Sunny")

elif temp >= 28 and not is_sunny:
    print("Its Hot Outside")
    print("Its Cloudy")

elif temp <=0 and not is_sunny:
    print("Its Cold Outside")
    print("Its Cloudy")

elif 28 > temp > 0 and not is_sunny:
    print("Its Warm Outside")
    print("Its Cloudy")

else:
    print("IDK!")