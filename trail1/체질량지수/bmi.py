height, weight = input().split();
height, weight = int(height), int(weight);

b = weight / ((height/100)**2);

print(f"{int(b)}")
if b >= 25:
    print("Obesity");