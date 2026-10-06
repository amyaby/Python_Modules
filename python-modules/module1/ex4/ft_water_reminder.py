def ft_water_reminder():
    rep=int(input("Days since last watering: "))
    if rep >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")