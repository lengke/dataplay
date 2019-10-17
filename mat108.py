from matplotlib import pyplot as plt

# 绘制多重条形图
# 重点在于x轴的偏移量设置

figure = plt.figure(figsize=(18, 10), dpi=80)

a = ["星球崛起3：\n终极之战", "吨科尔可", "蜘蛛侠：\n英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_spacing = 0.2

_a_14 = range(len(a))
_a_15 = [i+bar_spacing for i in _a_14]
_a_16 = [i+bar_spacing*2 for i in _a_14]

plt.bar(_a_14, b_14, width=bar_spacing, label="14日票房")
plt.bar(_a_15, b_15, width=bar_spacing, label="15日票房")
plt.bar(_a_16, b_16, width=bar_spacing, label="16日票房")

plt.xticks(_a_15, a, fontsize=14)

plt.ylabel("票房收入：元", fontsize=14)
plt.legend(fontsize=14)

plt.grid(alpha=0.3)
plt.show()
