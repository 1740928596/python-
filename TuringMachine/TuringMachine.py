import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

tapeLength = 1000  # 设置磁带的长度为1000
maxIter = 9999  # 设置最大迭代次数为9999

class TuringMachine:
    def __init__(self, programFile):
        self.tape = np.zeros(tapeLength)  # 初始化磁带，所有值设为0
        self.state = 1  # 设置图灵机的起始状态为0
        self.head = tapeLength // 2  # 将读写头初始化在磁带中间位置
        self.program = self.buildProgram(programFile)  # 从文件读取程序指令
        self.halt = True  # 初始化停机状态为True

    def buildProgram(self, programFile):
        """从给定的文件中读取并构建转换规则"""
        try:
            operators = [[]]  # 初始化操作列表
            with open(programFile, "r") as file:
                words = file.readlines()  # 读取文件的所有行
            # 处理每一行以构造操作步骤
            for word in words:
                parts = word.strip().split(",")  # 拆分每行为部分，并去掉换行符
                # 确保所有部分都存在，缺失的填充为"000"
                while len(parts) < 3:
                    parts = parts + ["000"]
                # 将解析和潜在更正后的行添加到操作中
                operators = operators + [[parts[1] or "000", parts[2] or "000"]]

            return operators
        # 错误判断
        except FileNotFoundError:
            print(f"Error: The file {programFile} was not found.")  # 文件未找到错误
            return []
        except Exception as e:
            print(f"An error occurred: {e}")  # 捕捉并打印其他异常
            return []

    def step(self):
        """执行图灵机的一步操作"""
        symbol = int(self.tape[self.head])  # 获取当前头部位置的磁带上的值
        command = self.program[self.state][symbol]  # 从程序中获取对应的指令
        if command == "000":  # 检查指令是否是停机状态
            self.halt = True
            return
        opt, move= command[0],command[1]  # 解析指令
        state_1 = int(command[2]) 
        self.tape[self.head] = int(opt)  # 更新磁带上当前头部位置的值

        # 根据指令移动磁带头部
        if move == "L":
            if self.head == 0:
                raise IndexError("Attempting to move left from the start of the tape.")
            self.head -= 1
        elif move == "R":
            if self.head == len(self.tape) - 1:
                raise IndexError("Attempting to move right from the end of the tape.")
            self.head += 1
        else:
            raise ValueError(f"Invalid move direction: {move}")

        self.state = state_1  # 更新到新状态

    def run(self, input_sequence):
        """将输入序列处理并运行图灵机"""
        converted_data = np.array([int(char) for char in input_sequence])  # 转换输入序列为整数数组
        input_length = len(input_sequence)
        if self.head + input_length > len(self.tape):
            raise ValueError("Input data extends beyond the tape length.")

        self.tape[self.head:self.head + len(converted_data)] = converted_data  # 采用替换方式在磁带上设置输入数据
        operation_count = 0  # 初始化操作计数器
        for _ in range(maxIter):  # 控制执行次数的循环
            if not (0 < self.state < len(self.program)) or not (0 <= self.head < len(self.tape)):
                break
            self.step()  # 图灵机执行指令
            operation_count += 1

        if operation_count >= maxIter or self.head >= len(self.tape) or self.head < 0:
            # 当超出磁带范围时
            self.tape = np.zeros(tapeLength)  # 重置磁带为0
        return operation_count #记录图灵机执行步数，有些文章中bb(n)指的是这个


    def getTuringResult(self):
        """获取图灵机运行后磁带上的结果"""
        return len(np.trim_zeros(self.tape))  # 返回去除前后0的磁带数据

    def getCurrentStateString(self):
        """返回当前图灵机的状态信息"""
        return f"当前状态：{self.state}，位置：{self.head}，tape状态：{self.tape}"
        
    def visualize(self):
        '''可视化功能，磁带太大了有点看不清'''
        fig, ax = plt.subplots()
        ax.set_xlim(450, 550)  # 设置x轴的范围，匹配磁带的长度
        ax.set_ylim(-0.5, 1.5)  # 设置y轴的范围，给头部位置和磁带值分别留出空间
        ax.set_title("Turing Machine Tape Visualization")  # 设置图表标题
        ax.set_xlabel("Tape position")  # 设置x轴标签
        ax.set_ylabel("Values")  # 设置y轴标签

        # 磁带值用红色圆点表示，减小了markersize
        tape_line, = ax.plot([], [], 'ro', markersize=3, label='Tape Values')
        # 头部位置用绿色圆点表示，减小了markersize，并移动到略高的y位置以区分
        head_line, = ax.plot([], [], 'go', markersize=3, label='Head Position')
        ax.legend()  # 添加图例

        def init():
            tape_line.set_data([], [])
            head_line.set_data([], [])
            return tape_line, head_line

        def update(frame):
            # 更新磁带上的点，y值设为0以便所有点在同一水平线上
            tape_line.set_data(range(len(self.tape)), [0] * len(self.tape))
            # 在磁带的相应位置显示值，将磁带值作为y值
            tape_data = [val if val != 0 else 0 for val in self.tape]  # 除去磁带上的零，便于视觉区分
            tape_line.set_ydata(tape_data)
            # 更新读写头的位置，y值设为1，使其位于磁带值上方
            head_line.set_data([self.head], [1])
            return tape_line, head_line

        # 创建动画，设置每帧调用update函数，不重复播放
        ani = FuncAnimation(fig, update, frames=range(maxIter), init_func=init, blit=True, repeat=False)

        plt.show()
        
# 示例使用：
if __name__ == "__main__":
    tm = TuringMachine("add.tr")  # 创建图灵机实例
    tm.run("111011111")  # 运行图灵机
    print(tm.getTuringResult())  # 打印结果
    print(tm.getCurrentStateString())  # 打印状态信息
    tm.visualize() #可视化样例

