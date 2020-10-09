N= 3
W= 8

sums= [0]*(W+2)

for i in range(N):
    w, val= map(int, input().split())

    for j in range(W+1, w-1, -1):
        print('w', w, 'j', j, sums[j-w], sums[j])
        sums[j]= max(sums[j-w] + val, sums[j])

    print(i, j, "    ", sums)

print(sums)

