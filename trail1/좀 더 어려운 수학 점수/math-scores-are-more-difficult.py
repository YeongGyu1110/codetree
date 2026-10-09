# 학생a
q,w = map(int, input().split());
# 학생b
e,r = map(int, input().split());

if (q>e):
    print('A');
elif (e>q):
    print('B');
else:
    if (w>r):
        print('A');
    elif (r<w):
        print('B');