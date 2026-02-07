fruit = ["apple", "orange", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]
groceries = [fruit, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end=" \n")
    print()
