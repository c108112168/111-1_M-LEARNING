# q_learning.py
# -*- coding: UTF-8 -*-
"""
Q Learning Algorithm
"""

import numpy as np
import pandas as pd


class QLearning:
    def __init__(self, actions, learning_rate=0.01, discount_factor=0.9, e_greedy=0.1):
        self.actions = actions  # action 列表
        self.lr = learning_rate  # 學習速率
        self.gamma = discount_factor  # 折扣因子
        self.epsilon = e_greedy  # 贪婪度
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float32)  # Q 表

    # 检测 q_table 中有没有这个 state
    # 如果还没有当前 state, 那我们就插入一组全 0 数据, 作为这个 state 的所有 action 的初始值
    def check_state_exist(self, state):
        if state not in self.q_table.index:

            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    # 根據 state 來決定 action
    def choose_action(self, state):
        self.check_state_exist(state)  # 檢查當前 state 是否在 q_table 中存在
        # 用 Epsilon Greedy 來選擇行為
        if np.random.uniform() < self.epsilon:
            # 隨機選 action
            action = np.random.choice(self.actions)
        else:  # 選擇 Q 直最高的 action
            state_action = self.q_table.loc[state, :]

            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.idxmax()
        return action

    # 学习。更新 Q 表中的值
    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)  # 检测 q_table 中是否存在 s_

        q_predict = self.q_table.loc[s, a]  # 根据 Q 表得到的 估计（predict）值

        # q_target 是现实值
        if s_ != 'terminal':  # 下个 state 不是 终止符
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r  # 下个 state 是 终止符

        # 更新 Q 表中 state-action 的數值
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)
