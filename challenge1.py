# 1
if 13%2==1:
    print("홀수")
else :
    print("짝수")

# 2
jumin = "881120-1068234"
first = jumin[:6]
last = jumin[7:]
print(first)  # 881120 출력
print(last)

# 3
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 4
i = 0
while True:
    i += 1

    if i<4 :
        print("*" * i)

    if i>2 :
        while True :
            i -= 1
            print("*" * i)
            if i==0 :
                break;
        break;

# 5
a=[1,2,3,4,5]
Result =[num*2 for num in a if num%2==1]
print(Result)