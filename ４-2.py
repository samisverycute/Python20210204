d={}
print("歡迎使用英文高手系統")
while True:
    print("1.建立辭彙")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5. 測驗學習成果")
    print("6.離開系統")
    op = input("Enter ur option")
    if op == "6":
        break
    elif op == "1":
        while True:
            voc = input("請輸入新單字(按0跳出)")
            if voc =="0":
                break
            if voc in d:
                print("單字已經存在")
            else:
                m = input("請輸入中文解釋")
                d[voc] = m
    elif op =="2":
        d1 = sorted(d)
        for i in d1:
            print(i,d[i])
    elif op == "3":
        voc = input("請輸入要查詢的英文單字")
        if voc in d:
            print(d[voc])
        else:
             print("字典沒有這個單字")
    elif op == "4":
         temp = False
         ch = input("輸入查詢的中文")
         for k,v in d.items():
             if ch == v:
                 print(ch,"的英文是",k)
                 temp = True
         if temp == False:
             print("字典沒有這個單字")
    elif op == "5":
        score = 0
        print("一共有",len(d),"題")
        for k,v in d.items():
            print(v,":")
            ans = input()
            if ans ==k:
                print("correct!")
                score = score + 1
            else:
                print("wrong!")
        print("一共得到",score,"分")
            
        
         
    
    