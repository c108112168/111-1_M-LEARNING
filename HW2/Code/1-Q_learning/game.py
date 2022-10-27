import pygame
import sys
import time
monster = [33, 37]
start_position = 97
step = 50
target = 4  # 目标位置
# 107是为了防止在初始位置往下走
wall = [107, 0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 19, 29, 39, 49, 59, 69, 79, 89, 99, 91, 92, 93, 94, 95, 96, 98]
kill_wait_time = 0.1
is_killed = False


class Mygame():
    def __init__(self):
        super(Mygame, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        # self.title("Q-learning shoot game")
        self.size = width, height = 500, 500  # 设置窗口大小
        self.screen = pygame.display.set_mode(self.size)  # 显示窗口
        # clock = pygame.time.Clock()  # 设置时钟
        self.background_color = (255, 255, 255)  # 设置颜色
        self.person = start_position
        self.monster = [33, 37]
        self.draw_map()

    def draw_map(self):
        """
        :param person:当前人的位置
        :param monster: 当前怪兽的位置
        :return:
        """
        # width、height已经给出
        rect = [0] * 110
        self.screen.fill(self.background_color)  # 填充颜色(设置为0，执不执行这行代码都一样)
        for i in range(10):
            for j in range(10):
                curr_rect = 10 * i + j
                if target == curr_rect:
                    # 绿色表示终点
                    rect[curr_rect] = pygame.draw.rect(self.screen, (0, 228, 0), ((j * step, i * step), (step, step)), width=0)
                elif curr_rect in wall:
                    # 灰色表示墙
                    rect[curr_rect] = pygame.draw.rect(self.screen, (192, 192, 192), ((j * step, i * step), (step, step)), width=0)
                elif curr_rect == self.person:
                    # 红色表示人
                    rect[curr_rect] = pygame.draw.rect(self.screen, (192, 0, 0), ((j * step, i * step), (step, step)), width=0)
                elif curr_rect in monster:
                    # 画出怪兽
                    rect[curr_rect] = pygame.draw.rect(self.screen, (138, 43, 226), ((j * step, i * step), (step, step)), width=0)
                else:
                    # 其余填充白色
                    rect[curr_rect] = pygame.draw.rect(self.screen, (255, 228, 181), ((j * step, i * step), (step, step)), width=1)
        pygame.display.update()

    def judge_win(self):
        """
        如果人到达终点， 则胜利
        :return: True or False
        """
        if self.person == target and is_killed == True:
            return True
        else:
            return False

    def reset(self):
        self.person = 97
        self.monster = [33, 37]
        print(self.person)
        return self.person, self.monster

    def judge_collision(self, temp_person):
        """判断人是否碰撞到墙或怪物"""
        if temp_person in wall or temp_person < 0:
            return True
        else:
            return False

    def kill_monster(person, monster):
        """
        人静止两秒且怪物在攻击范围内才能杀死怪物
        人的攻击范围是：
        :param person:人当前的位置
        :param monster: 怪兽当前的位置
        :return: 返回怪兽坐标， 如果杀死怪兽了返回[-1, -1]
        """
        #if time < kill_wait_time:
            # print("time short")A
            # 攻击时间小于两秒直接返回， 杀不死怪兽
            #return monster
        attack_area = [person-1, person-2, person-3, person, person + 1, person+2, person + 3,\
                   person-13, person-12, person - 11, person - 10, person - 9, person - 8, person -7,\
                   person-23, person-22, person - 21, person - 20, person - 19, person - 18, person -17,\
                   person+13, person+12, person + 11, person + 10, person + 9, person + 8, person + 7]
        if monster[0] in attack_area:
            print("kill monster!")
            return [-1, -1,-1]
        else:
            print("not kill monster!")
            return monster

        # 走一步（机器人实施 action）

    def step(self, action):
        # s状态
        s = self.person

        # 移动机器人, 直接更新下一个state
        if action == 0:  # 上
            s_ = s - 10
            is_collision = self.judge_collision(s_)
            #if s_ > 23:
             #   self.kill_monster(self.person)
            if is_collision:
                s_ = s
        elif action == 1:  # 下
            s_ = s + 10
            is_collision = self.judge_collision(s_)
            if is_collision:
                s_ = s

        elif action == 2:  # 右
            s_ = s + 1
            is_collision = self.judge_collision(s_)
            if is_collision:
                s_ = s

        elif action == 3:  # 左
            s_ = s - 1
            is_collision = self.judge_collision(s_)
            if is_collision:
                s_ = s

        # 獎勵
        if s_ == target:
            # 通關獎勵 1
            reward = 1
            done = True
            # 結束
            s_ = 'terminal'
            print("通關,很不錯喔!")
        elif s_ in monster:
            # 碰到怪物
            # 獎勵-1
            reward = -1
            done = True
            # 結束
            s_ = 'terminal'
            print("Fight with monster!")
        else:
            # 正常,不好不壞
            reward = 0
            # 繼續
            done = False
        return s_, reward, done
