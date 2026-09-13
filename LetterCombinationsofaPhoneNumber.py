dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

num = input().strip()

if num == "":
    print([])
else:
    arr = ['']   
    for i in range(len(num)):
        temp = []
        for prefix in arr:
            for ch in dict[num[i]]:
                temp.append(prefix + ch)
        arr = temp
    
    print(' '.join(arr))