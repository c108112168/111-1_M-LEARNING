# main.py
# -*- coding: UTF-8 -*-

"""
游戏的主程序，调用q_learning和env
"""

from game import Mygame
from q_learning import QLearning
import pygame
import matplotlib.pyplot as plt
import pandas as pd

def update():
    for episode in range(100):  # 100次游戏情节
        # 初始化 state（状态）
        state = env.reset()
        print(state)

        step_count = 0  # 记录走过的步数

        while True:
            # 更新可视化环境

            clock = pygame.time.Clock()  # 设置时钟
            clock.tick(10)  # 每秒执行100次
            # RL 大脑根据 state 挑选 action
            action = RL.choose_action(str(state))
            # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state, reward 和 done (是否是踩到炸弹或者找到宝藏)
            state_, reward, done = env.step(action)
            # print(state_)
            step_count += 1  # 增加步数

            # 机器人大脑从这个过渡（transition） (state, action, reward, state_) 中学习
            RL.learn(str(state), action, reward, str(state_))

            # 机器人移动到下一个 state
            state = state_
            env.person = state

            env.draw_map()
            # 如果踩到炸弹或者找到宝藏, 这回合就结束了
            if done:
                print("回合 {} 结束. 总步数 : {}\n".format(episode + 1, step_count))
                break

    # 结束游戏并关闭窗口
    print('游戏结束')
    pygame.quit()


if __name__ == "__main__":
    # 创建环境 env 和 RL
    pygame.init()  # 初始化pygame
    env = Mygame()
    RL = QLearning(actions=list(range(env.n_actions)))

    # 执行update函数
    update()
    plt.plot(x1, LeBron.PTS, color='b')
    plt.xlabel('TIMES')  # 設定x軸標題
    plt.xticks(LeBron.SEASON_ID, rotation='vertical')  # 設定x軸label以及垂直顯示
    plt.title('LeBron James')  # 設定圖表標題
    plt.show()
    print('\nQ table:')
    print(RL.q_table)

