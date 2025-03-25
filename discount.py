def calculate_discount(price, discount_percent):
    # if the discount is 20% or higher, apply the discount; otherwise, return the original price
    if discount_percent >= 20:
        discounted_amount = price * (discount_percent / 100)
        final_price = price - discounted_amount
        return final_price
    else:
        return price

# prompt the user to enter the original price of an item and the discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# print the final price after applying the discount, or if no discount was applied, print the original price
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price is: {final_price}")