def fractional_knapsack(items, capacity):
    # مرتب کردن آیتم‌ها بر اساس ارزش به وزن
    items = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)

    total_value = 0
    for item in items:
        if capacity >= item["weight"]:
            capacity -= item["weight"]
            total_value += item["value"]
        else:
            # انتخاب بخشی از آیتم
            fraction = capacity / item["weight"]
            total_value += item["value"] * fraction
            break

    return total_value


items = [
    {"value": 60, "weight": 10},
    {"value": 100, "weight": 20},
    {"value": 120, "weight": 30}
]

capacity = 50
max_value = fractional_knapsack(items, capacity)
print("Max value:", max_value)
