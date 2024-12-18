def lonelyinteger(a):
    # Write your code here
    
    num_occur = {}

    for x in a:
        num_occur[x] = 0
    
    for x in a:
        num_occur[x] += 1
        
    return [key for key, value in num_occur.items() if value == 1][0]

a = [1,2,3,4,3,2,1]

print(lonelyinteger(a))