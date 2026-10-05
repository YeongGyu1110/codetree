a,b = list(map(int, input().split()));
firRes = 0;
secRes = 0;

if a<b:
    firRes = 1;
else:
    firRes = 0;

if a==b:
    secRes = 1;
else:
    secRes = 0;

print(firRes, secRes)