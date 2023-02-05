def sz(n):
  out=[]
  r=n//2
  for i in range (1,r+1):
    out.append (i)
    out.append(-i)
  if n%2!=0:
    out.append (0)
  return out
