a = True
print(a:=False)

foods = []

# while True:
#     food = input("enter a food would you like:-")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

while (food:= input('enter the food')) != 'quit':
    foods.append(food)
print(foods)

sample_data = [
    {"userid":1,"name":"yash","city":"morbi"},
    {"userid":2,"name":"Shubham","city":"Rajkot"},
    {"userid":3,"name":"Kalyan","city":"Baroda"},
    {"userid":4,"name":"shivay","city":"new york"},
    {"userid":5,"name":"shiv","city":"nagasaki"}
]
#using the warlus operator
for entry in sample_data:
   if name:= entry.get("name"):
       print(f"found name:-{name}")

#without the warlus operator
for entry in sample_data:
    name = entry.get("name")
    print(f"found the name:-{name}")
