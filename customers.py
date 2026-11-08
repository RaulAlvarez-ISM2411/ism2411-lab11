# Exercise 1 

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2 

customer["phone"] = "305-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

 # Exercise 4 

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount = tier_discounts.get(customer["tier"], 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", customer["tier"])
print("Discount rate:", discount * 100, "%")
print("Final price:", final_price)

# Exercise 6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for customer in customers:
    discount = tier_discounts.get(customer["tier"], 0)
    discount_amount = 300 * discount

    print(f'{customer["name"]} - {customer["tier"]} - Discount: ${discount_amount:.2f}')

# Exercise 7

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left!")

# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region, total in sorted(sales_by_region.items()):
    print(f"{region}: ${total}")