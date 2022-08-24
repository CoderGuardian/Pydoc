op_set=('+','-','*','/')
num,flag="",'Y'
while flag=='Y':
    exp=input("Enter the Expression = ")
    i=0
    while exp[i] not in op_set:
        num=num+exp[i]
        i+=1
    nums1=int(num)
    op,num=exp[i],""
    print(op)
    while i<len(exp):
        num=num+exp[i]
        i+=1
    nums2=int(num)

    if op == '+':
        print("Answer = ", nums1+nums2)
    elif op == '-':
        print("Answer = ", nums1-nums2)
    elif op == '*':
        print("Answer = ", nums1*nums2)
    elif op == '/':
        print("Answer = ", nums1/nums2)
    else:
        print("Invalid Input")

    flag=input("Continue > (Y) ")