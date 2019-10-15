from matplotlib import pyplot as plt

"""
独立作业
"""
# 建立figure对象
figure = plt.figure(figsize=(18, 10), dpi=80)

# 设定x,y轴的数值
x = range(1, 13, 1)
y1 = [5000, 4500, 5100, 3000, 7000, 4200, 6600, 9100, 5800, 6000, 4000, 7200]
y2 = [4000, 3500, 4600, 3700, 8500, 3900, 5700, 6300, 4400, 7000, 5200, 8000]

# 调整XY轴刻度
_x = range(1, 13, 2)
plt.xticks(_x, [str(i) + "月" for i in _x], fontsize=13)
_y = range(2000, 11000, 1000)
plt.yticks(_y, [str(t) + "元" for t in _y], fontsize=13)

# 设置图中标注
plt.annotate("最高点", (8, 9000), (8.1, 9000), fontsize=14)
plt.annotate("最低点", (4, 3000), (4.1, 3000), fontsize=14)

# 设置背景网格线
plt.grid(alpha=0.4)

# 画图并设置图例内容与线条属性
plt.plot(x, y1, linestyle="--", label="张三", color="red")
plt.plot(x, y2, linestyle=":", label="李四", color="green")
# 绘制图例
plt.legend(loc="upper left", fontsize=14)
# 设置图表标题
plt.title("张三、李四每月支出图", fontsize=20)

plt.show()
# plt.savefig("./temp/t.png")
