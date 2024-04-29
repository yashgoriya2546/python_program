
# String are immutable
a = "!!!!!!yash,goriya!!!! !!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("goriya", "Patel"))
print(a.split(" "))

blogheading = "introduction about python programing language....."
print(blogheading.capitalize())

str1 = "wel-come to python tutorial"
print(len(str1))
print(len(str1.center(50)))
print(a.count("yash"))

str1 = "Welcome to console!!!"
print(str1.endswith("&&&"))
print(str1.endswith("to" , 4 , 10))

str2 = "he is a Dan.he is an honesht man"
print(str2.find("is"))

str1 = "Welcome to the console"
print(str1.isalnum())

str1 = "Good morningX"
print(str1.isalpha())

str1 = "hellow world"
print(str1.islower())

str1 = "we wish you a merry christmas\n"
print(str1)
print(str1.isprintable())

str2 = " " #using a spaacebar
print(str2.isspace())

str2 = "    " # using a tab
print(str2.isspace())

str1 = "World Health Oraganization" # it is a title..
print(str1.istitle())

str1 = "world health Oraganization" # it is a not title..
print(str1.istitle())

str1 = "python is a interprited language"
print(str1.startswith("python"))

str1 = "c++ is hard programing language"
print(str1.endswith("language"))

str1 = "His name is Dan.Dan is an honest man" # swapcase is used to uppercase convert to lowercase ans lowercase convert to uppercase....
print(str1.swapcase())

str1 = "hyy good morning"
print(str1.title())
