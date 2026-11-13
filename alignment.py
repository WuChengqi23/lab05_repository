items = [("Apple", 0.99, 5), ("Bread", 2.49, 2), ("Milk", 1.29, 3)]

print(f"{'Item':<12} {'Price':>8} {'Qty':>5} {'Total':>8}")
print("-" * 36)

for name, price, qty in items:
    total = price * qty
    print(f"{name:<12} {price:>8.2f} {qty:>5} {total:>8.2f}")