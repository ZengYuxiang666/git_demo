# 请在此输入您的代码
def cul(aa,Z):
  l=0
  r=len(aa)-1
  ans=0
  while l<r:
    if aa[l]+aa[r]<=Z:
      ans+=r-l
      l+=1
    else:
      r-=1
  return ans

n,L,R=map(int,input().split())
aa=list(map(int,input().split()))
aa.sort()
print(cul(aa,R)-cul(aa,L-1))

