result = []
reverse_name = ''
while True:
    n = input()
    if(n == "END"):
        break

    result = list(n)
    result.reverse()

    for c in n: reverse_name = c + reverse_name

    r = ''.join(result)
    print(r)
    
