def modDiv(P,Q,mod): # P/Q mod m
  denominator = pow(Q,-1,mod)
  return P*denominator%mod