def multiplier_generator(base):
    def multiplier(x):
        if base == 0:
            return x * x  
        else:
            return base * x
    return multiplier


doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)  


if __name__ == "__main__":
    print("Doubler:")
    print(f"2 * 5 = {doubler(5)}")  
    print(f"2 * 8 = {doubler(8)}")  

    print("\nTripler:")
    print(f"3 * 4 = {tripler(4)}")  
    print(f"3 * 7 = {tripler(7)}")  

    print("\nSquarer (Special Case):")
    print(f"Square of 6 = {squarer(6)}")  
    print(f"Square of 9 = {squarer(9)}")  
