N,n = int(input()),list(map(int,input().split()))
print(all(int(i)>0 for i in n) and any([(int(str(abs(i))[::-1]) == i) for i in n]))