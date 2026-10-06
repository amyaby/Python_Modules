def  ft_count_harvest_iterative():
    icc = int(input("Days until harvest:"))
    for i in range(icc):
        print(f"Day {i+1}")
    if i == icc:
        print("Harvest time")