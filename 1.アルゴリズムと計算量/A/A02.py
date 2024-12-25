input_text = input()
input_num = list(map(int,input_text.split()))
x = input_num[1]
a = list(map(int, input().split()))
if x in a:
    print('Yes')
else:
    print('No')