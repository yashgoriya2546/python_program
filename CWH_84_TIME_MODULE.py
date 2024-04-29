# import time
#
# def whileloop():
#     i  = 0
#     while i<50:
#         print(i)
#         i = i + 1
#
# def forloop():
#     for i in range(50):
#         print(i)
#
#
# init = time.time()
# whileloop()
# t1 = (time.time() - init)
# init = time.time()
# forloop()
# print(time.time() - init)
# print(t1)

import time

print("Hey Good morning Everyone")
time.sleep(5)
print("very good morning")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d-%H:%M:%S %Z%z",t)

print(formatted_time)