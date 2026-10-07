a,b,c = list(map(int, input().split()));

res1 = 0;
res2 = 0;


if a<=b and a<=c:
    min = a;
elif b<=a and b<=c:
    min = b;
elif c<=a and c<=b:
    min = c;

if a == min:
    res1 = 1;

if a==a and a==b and a==c:
    res2 = 1;
else:
    res2 = 0;

print(res1, res2)