import time

m = input("Enter your Name: ").lower()
f = input("Enter their Name: ").lower()
print()

fcount = 0
scount = 0

for i in m :
    if i in "true" :
        fcount += 1
for j in f :
    if j in "true" :
        fcount += 1

for p in m :
    if p in "love" :
        scount += 1
for q in f:
    if q in "love" :
        scount += 1

time.sleep(1)

print("CALCULATING LOVE PERCENTAGE",end="")

for i in range(3) :
    time.sleep(1)
    print(".",end="")

time.sleep(2)
print()

lcount = int(str(fcount) + str(scount))

if lcount < 35 :
    print(f"Your Love Percentage is: {lcount}% \nThey don't love you that much! :P ")
elif lcount > 35 and lcount < 70 :
    print(f"Your Love Percentage is: {lcount}% \nYou both are a good  match! ")
else:
    print(f"Your Love Percentage is: {lcount}% \nyou both are perfect together!!")


