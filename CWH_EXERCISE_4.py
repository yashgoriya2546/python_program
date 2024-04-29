questions = [["which language was used to create fb?","python","java","php","franch","none",4],
             ["name of the prime-minister of India?","Amit shah","Narendra modi","vijay rupani","yogi","none",2],
             ["which language was used to create fb?","python","java","php","franch","none",4],
             ["which language was used to create fb?","python","java","php","franch","none",4],
             ["which language was used to create fb?","python","java","php","franch","none",4],
             ["which language was used to create fb?","python","java","php","franch","none",4],
             ["which language was used to create fb?","python","java","php","franch","none",4]]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for RS.{levels[i]}")
    print(f"a.{question[1]} b.{question[2]}")
    print(f"c.{question[3]} d.{question[4]}")
    replay = int(input("Enter your correct answer:\n"))

    if replay == 0:
        money = levels[i-1]
        break
    if replay == question[-1]:
        print(f"correct answer,you have won RS.{levels[i]}")

        if i==4:
            money = 10000
        elif i==9:
            money = 320000
        elif i==14:
            money = 10000000
    else:
        print("wrong Answer!")
        break
print(f"your take home money is{money}")