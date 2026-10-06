#input() always returns a string (str) thats why we have to convert to int
# a number 2 is represented as "2"<==> "hello" bothare strings
def  ft_plot_area():
    length =int(input ("Enter length: "))
    print(type(length)) 
    width = int(input("Enter width: "))
    print(type(width)) 

    erea = length * width
    print(f"Plot area: {erea}")
def main():
    res = ft_plot_area()
    #print(res)
if __name__ == "__main__":
    main()