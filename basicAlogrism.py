# def pow(a,b,n):
#     product=1
#     for i in range(b):
#         product*=a
#         if(product>=n):
#             product%=n
#     return product%n
def PowerMod(a,b,c):
    ans = 1
    a = a % c
    while(b>0):
        if(b % 2 == 1):
            ans = (ans * a) % c
        b = b//2
        a = (a * a) % c
    return ans