pattern=input()
genome=input()

n=len(genome)
k=len(pattern)

for i in range(0, (n-k+1)):
    if(genome[i:i+k]==pattern):
        print(i,end=' ')