age = int(input("Your age: "))

if age > 14:
    print("Нельзя купить билет")
elif age == 14:
    print("OK")
else:
    print("Купить еще можно")

users = ["John", "Martin", "Nikita"]

for user in users:
    print("Hello, " + user)

counter = 0
while counter < 10:
    print(counter)
    counter += 1
