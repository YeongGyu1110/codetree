a,b = map(int, input().split());

target = a;
for i in range(21):
    if i == 0:
        print(a//b, end='.');
        target = a%b;
        continue;
    
    if b > target:
        target *=10;
        print(target//b, end='');
        target = target%b;