q,w = map(int, input().split());

if (q < 90):
    print(0);
elif (w >= 95):
    print(100000);
elif (w >= 90):
    print(50000);
else:
    print(0)