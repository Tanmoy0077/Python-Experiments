# import os
# os.chdir(os.path.join("E:\Temporary Storage\Problem"))
# count = 0
# for file in os.listdir():
#     os.rename(file, f"IMG {count}.jpg")
#     count += 1
# print(f"{count} Files renamed successfully")

for i in range(1, 1250):
    r1 = 650%i
    r2 = 775%i
    r3 = 1250%i
    if r1 == r2 and r2 == r3:
        print(r1, r2, r3)