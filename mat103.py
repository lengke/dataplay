from matplotlib import pyplot as plt

# ctl + . 折叠代码
# alt+shift+l 自动格式化代码

figure = plt.figure(figsize=(14, 8), dpi=80)
# 绘图数据
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
z = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
_xticks = [str(i) + "岁" for i in x]
plt.xticks(x, _xticks)
plt.yticks(range(0, 10))
# 绘制网格, alpha参数控制透明度
plt.grid(alpha=0.8, linestyle=":")
# 设置轴刻度和表格信息
plt.title("每年交女朋友数量走势")
plt.xlabel("岁数")
plt.ylabel("个数")

# 自定义绘制参数，线条形状、粗细，线条颜色、透明度
plt.plot(x, y, label="自己", color="red", alpha=0.8, linestyle="--", linewidth=2, marker="o")
plt.plot(x, z, label="同桌", color="green", linestyle="--", marker="*")
# 添加图表中的注释
plt.annotate("最高值", (23, 6), (23, 6.1))
plt.annotate("最低值", (12, 0), (12.2, 0))

# 添加图例：先在plt方法添加label参数，再调用legend()方法才行。
# loc参数控制legend的出现位置，0为best, 1:upper right, 2:upper left, 3:lower left, 4: lower right
plt.legend(loc="upper left")
plt.show()
