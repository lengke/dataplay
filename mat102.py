from matplotlib import pyplot as plt
import random
figure = plt.figure(figsize=(12, 8), dpi=80)

# 10-12点每一分钟的气温，共计120分钟
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 调整X轴刻度
_x = list(x)
_xtick_labels = [f"10点{i}分" for i in range(60)]
_xtick_labels += [f"11点{i-60}分" for i in range(60, 120)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)

plt.plot(x, y)
plt.show()



