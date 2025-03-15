def calculate_discount(price, discount_percent):
    """A function that calculates the final price after applying a discount"""
    
    # If discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_price = (discount_percent / 100) * price
        final_price = price - discount_price
    else:
        final_price = price
    
    # Formatting the final price to show 2 decimal places
    price_to_pay = f"Amount to pay is KSH {final_price:.2f}"

    return price_to_pay


#Prompt the user to input price and discount percent
price = float(input("Please enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))
        
# Call the calculate_discount function
result = calculate_discount(price, discount_percent)
        
# Print the result
print(result)
