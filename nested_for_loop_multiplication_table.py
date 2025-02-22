# BRYANT RAY M. MANALAD
# ITELEC2
# Laboratory #14 - Guided Coding Exercise: Nested for loop to print a Mutiplication Table

def main():
    
    for i in range(1, 6):
        for j in range(1, 6):
            #calculate the product
            product = i * j
            # Print the product with formatting
            print(f"{product:4}", end="")
        # New line after each row
        print()

    

if __name__ == "__main__":
    main()
    
