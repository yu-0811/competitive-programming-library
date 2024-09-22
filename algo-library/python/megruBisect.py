def megru_bisect(ng,ok):
  def judge(mid):
  
  while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if judge(mid): # 条件を満たすなら
      ok = mid
    else:
      ng = mid

  return ng,ok