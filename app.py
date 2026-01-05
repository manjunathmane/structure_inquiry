import sys

if len(sys.argv) != 4:
    print("Usage: python app.py <price> <discount> <quantity>")
    sys.exit(1)

price = float(sys.argv[1])
discount = float(sys.argv[2])
quantity = int(sys.argv[3])

total_price = price * quantity
discount_amount = total_price * discount / 100
final_price = total_price - discount_amount

print(f"Price per item: {price}")
print(f"Quantity: {quantity}")
print(f"Discount: {discount}%")

if final_price > 0:
    print(f"Final Price: {final_price}")
elif final_price == 0:
    print("Final price is zero")
else:
    print("Invalid calculation")
