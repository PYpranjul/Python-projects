# print("WELCOME TO KAUN BANEGA KISKA PATI")
# questions=["what is the Capital of India?","What is the Capital of Uttar pradesh"]
# answer=["(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi"]
# print("Ques No. 1",questions[0:1])
# print(answer)
# A=input("Select option: ")
# if (A=="B"):
#     print("Badhai ho 1000rupiya tumhra")
# else:
#     print("Afsoos")
# print("Ques no. 2",questions[1:2])




a=print("Kaun banega kiska pati")
qn=[["what is the capital of India? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2],
   ["what is the capital of Uttar Pradesh? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",3],
   ["what is the capital of India? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2],
   ["what is the capital of India? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2],
   ["what is the capital of India? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2],
   ["what is the capital of India? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2],
   ["what is the capital of Haryana? ","(A)Chandigarh","(B)New Delhi","(C)Lucknow","(D)Delhi",2]]
level=[1000,2000,4000,8000,20000,40000,100000]
money=0
for i in range(0,len(qn)):
    q=qn[i]
    print(f"Question no, {i+1} for Rs.{level[i]}")
    print(f"\n {q[0]}")
    # print(f"{q[0]}")
    print(f"{q[1]}                    {q[2]}")
    print(f"{q[3]}                       {q[4]}")
    reply=int(input("Enter the option: "))
    if reply==q[5]:
        print(f"Congratulations you have won Rs. {level[i]}")
        if i==3:
            money=8000
    else:
        print("Afsoos Har gaye ree")
        break
print("Tumko itta rupiya milye Rs.",money)