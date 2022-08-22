flag='y'
while flag=='Y' or flag=='y':
    exp=input("Enter expression : ")
    ans=eval(exp)
    print(exp+"="+str(ans))
    flag = input("Continue? (Y/N): ")
