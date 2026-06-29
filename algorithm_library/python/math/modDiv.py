def modDiv(P,Q,mod): # P/Q mod m
    denominator = pow(Q,-1,mod) # Q が同じなら前計算したほうが速い
    return P*denominator%mod