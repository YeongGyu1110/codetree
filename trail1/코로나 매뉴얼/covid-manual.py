a_cold, a_tem = input().split();
a_tem = int(a_tem);

b_cold, b_tem = input().split();
b_tem = int(b_tem);

c_cold, c_tem = input().split();
c_tem = int(c_tem);

if (a_cold == 'Y' and b_cold == "Y" and a_tem >= 37 and b_tem >= 37) or (a_cold == "Y" and c_cold == 'Y' and a_tem >= 37 and c_tem >= 37) or (b_cold=='Y' and c_cold == "Y" and b_tem >= 37 and c_tem >= 37):
        print("E");
else:
    print("N")