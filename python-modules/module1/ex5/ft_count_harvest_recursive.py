def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day):
        if day > days:
            print("Harvest time!")
            return

        print(f"Day {day}")
        count(day + 1)

    count(1)

def main():
    ft_count_harvest_recursive()

if __name__ == "__main__":
    main()
