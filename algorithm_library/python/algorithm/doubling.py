def doubling(dp,LEN,POW):
  for i in range(1,POW):
    for j in range(LEN):
      dp[i][j] = dp[i-1][dp[i-1][j]]
  return dp

def query(dp,j,k):
  tmp = j
  i = 0
  while k:
    if k&1: tmp = dp[i][tmp]
    k >>= 1
    i += 1
  return tmp