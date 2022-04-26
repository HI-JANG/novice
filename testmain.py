n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    cnt = 0
    for i in a[1:]:
        if avg < i:
            cnt +=1
    rate = round(cnt/a[0]*100,5)
    print(f'{rate:.3f}%')



