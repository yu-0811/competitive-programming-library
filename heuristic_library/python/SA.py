import sys
def input():return sys.stdin.readline().rstrip()
def ii(): return int(input())
def ms(): return map(int, input().split())
def li(): return list(map(int,input().split()))
def print_err(*args): print(*args,file=sys.stderr)
from random import randrange,randint,random
from time import time
start = time()

from math import exp
# パラメータ ##############################
start_temp = 500
end_temp = 10
time_limit = 1.85 # 単位 : s
###########################################

# 線形温度管理
def linear_temp(SA_start_time : float, now_time : float) -> float:
  return start_temp - (start_temp - end_temp) * (now_time - SA_start_time) / time_limit

# 遷移確率関数
# スコア最大化のとき
def calc_prob_maximize(now_score, next_score, temp) -> float:
  return 1 if now_score < next_score else exp((now_score - next_score) / temp)

# スコア最小化のとき
def calc_prob_minimize(now_score, next_score, temp) -> float:
  return 1 if now_score > next_score else exp((next_score - now_score) / temp)

# グローバル変数 #########################

##########################################

def calc_score():

  return

def initialize_score():

  return

# 近傍生成 + スコア計算 + 受容判定 -> 新しいスコアを返す
def generate_neighbor(now_score : int|float, temp : float):
  # 近傍生成 ######################

  ################################
  # スコア計算 ###################
  next_score = 
  if (calc_prob_maximize(now_score, next_score, temp) > random()): # 受容する
    # 必要であれば状態を更新 ######
    
    ###############################
    return next_score
  else: # 受容しない
    # 状態を元に戻す #############

    ##############################
    return now_score
  
def SA():
  SA_start_time = time()
  iter = -1
  temp = start_temp
  # スコアの初期化
  now_score = initialize_score()
  while True:
    if (iter%500 == 0):
      now_time = time()
      if (now_time - start > time_limit):
        break
      temp = linear_temp(SA_start_time, now_time)
    now_score = generate_neighbor(now_score, temp)
    iter += 1
  print("SA DONE", iter, file=sys.stderr)

SA()

# 出力 ############################

##################################