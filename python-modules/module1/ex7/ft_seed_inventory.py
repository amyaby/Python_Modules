def  ft_seed_inventory(s_type:str,nbr:int,quant:str)-> None:
    if(s_type == "tomato"):
        print(f"Tomato seeds: {nbr} {quant} available")
    elif(s_type == "carrot"):
        print(f"Carrot seeds: : {nbr} {quant} total")
    elif (s_type == "lettuce"):
        print(f"Lettuce seeds: covers {nbr} square meters")
    else:
        print("Unknown seed type")
#def main():
#    ft_seed_inventory("tomato", 15, "packets")
#if __name__ == "__main__":
#    main()