print("Xin chao moi nguoi")
a=7
b=5
c=a-b
print(c)
city="Hà Nội"
year=2025
print("Thành phố:",city,"-Năm:",year)
n=4
t=0
for i in range(1,n+1):
    t += i
    print(t)
numbers = [1, 2, 3, 4] 
for x in numbers: 
    if x % 2 == 0: 
        print(x, "là số chẵn") 
    else: 
        print(x, "là số lẻ") 
animals = ["cat", "dog", "cat", "bird"] 
count = 0 
for a in animals: 
    count += 1 
    print("Số phần tử trong danh sách là:", count)
num = int(input("Nhập số: "))
if num % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")