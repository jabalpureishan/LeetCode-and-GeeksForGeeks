def N_Sum(N):
  return((N*(N+1))//2)

def terms(N):
  Ans,Power = 0,0
  while(Ans<=N):
    Ans = 2**Power
    Power = Power + 1
  return(Power-1)

def Progression(T):
  A = 2**T - 1
  return(A)

T = int(input(""))
for i in range(T):
  N = int(input(""))
  T = terms(N)
  Result  = N_Sum(N) - 2*(Progression(T))
  print(Result)