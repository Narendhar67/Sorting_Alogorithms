def arrayManipulation(n, queries):
    # Write your code here
    
    ans=[0 for i in range(n)]
    for i in queries:
        ans[i[0]-1]+=i[2]
        if i[1]<len(ans):
            ans[i[1]]-=i[2]
    s=0;maxi=0
    for i in range(len(ans)):
        s+=ans[i]
        maxi=max(maxi,s)
    return maxi