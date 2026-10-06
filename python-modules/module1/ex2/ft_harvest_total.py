def  ft_harvest_total():
    total = 0
    for i in range(3):
        total += int(input(f"Day{i+1} harvest:"))
        #harvest += int(input(f"Day{i+1} harvest:"))
        # total += harvest
    print(f"Total harvest: {total}")