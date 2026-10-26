text=input()
reverse=text[::-1]
reverse_compliment=""

for ch in reverse:
    if(ch=='A'):
        reverse_compliment+='T'
    elif(ch=='C'):
        reverse_compliment+='G'
    elif(ch=='G'):
        reverse_compliment+='C'
    elif(ch=='T'):
        reverse_compliment+='A'

print(reverse_compliment)