N = int(input())
positive = True
palindromic = False
for i in (list(map(int,input().split()))):
    if i <= 0:
        positive = positive and False
    if int(str(abs(i))[::-1]) == i:
        palindromic = palindromic or True
        
print(positive and palindromic)