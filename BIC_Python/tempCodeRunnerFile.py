def Pateern_count(text, pattern):
    count=0
    k=len(pattern)
    for i in range (len(text)-k+1):
        if text[i:i+k]==pattern:
            count+=1
    return count
text=input()
pattern=input()
#text="ACAACTATGCATACTATCGGGAACTATCCT"
#pattern="ACTAT"
print("The number of Appears: ",Pateern_count(text,pattern))
