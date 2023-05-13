# 状態s(t)...時刻tでの、cartの位置x,速度v,棒の角度θ,棒の角速度ωの4次元で表現される。
# s(t) = [x(t), v(t), θ(t), ω(t)]
# 行動a(t)...cartを右におすか、左におすかの選択。我々にできる行動はこれだけ。

import gym
from gym import wrappers
import numpy as np
import time

# Q関数を離散化して定義する関数
# 観測した状態を離散値にデジタル変換する...周波数みたいなイメージ？
# 指定した範囲の値を、num等間隔に分割にします。
# num+1と[1:-1]は何？
def bins(clip_min, clip_max, num):
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

# 各値をデジタルにする
# digitize...指定されたビンのうち、その変数の値がビンの何番目にに属するかを示す。
# digittize関数のbins引数は、境界値の配列を受け取るため、0と1の区間を2分割したい場合、境界値は[0,0.5,1]の3つある。よって、n等分するには、以下のようにすべし。
# binsに、等間隔に区切られた境界値が渡される。[0, 0.5, 1]
# ///////////////////////////////////////////////////
# import numpy as np
# bins = np.linspace(0, 1, n+1)
# dist = np.digitize(0, bins)
# ///////////////////////////////////////////////////
def digitize_state(observation):
    cart_pos, cart_v, pole_angle, pole_v = observation
    digitize = [
        np.digitize(cart_pos, bins=bins(-2.4, 2.4, num_digitized)),
        np.digitize(cart_v, bins=bins(-3.0, 3.0, num_digitized)),
        np.digitize(pole_angle, bins=bins(-0.5, 0.5, num_digitized)),
        np.digitize(pole_v, bins=bins(-2.0, 2.0, num_digitized)),
    ]
    return sum([x * (num_dizitized **i) for i, x in emurate(digitized)])

# 行動a(t)を求める関数
def get_action(next_state, episode):
    #徐々に最適行動を取る、ε-greedy法
    epsilom = 0.5 * (1 / (episode + 1))
    if epsilon <= np.random.uniform(0, 1):
        next_action = np.argmax(q_table[next_state])
    else:
        next_action = np.random.choice([0, 1])
    return next_action 
