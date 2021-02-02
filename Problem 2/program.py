N = int(input('Enter the range:'))
X = int(input('Enter the number:'))
Y = int(input('Ener the secont number:'))
sum=0
for i in range(N):
    if (i%X==0) or (i%Y==0):
        sum+=i
required_sum = sum
reverse_sum = 0
while sum>0:
    a = sum%10
    reverse_sum = reverse_sum*10 + a
    sum = sum//10

print(required_sum)
print(reverse_sum)
