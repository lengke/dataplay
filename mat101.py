from matplotlib import pyplot as plt

fig = plt.figure(figsize=(15, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
# 绘图
plt.plot(x, y)
# 绘制X轴的刻度
# plt.xticks(range(2, 25, 1))
_xticks = [x/2 for x in range(2, 49)]
plt.xticks(_xticks[::3])
# 调整Y轴刻度
# plt.yticks(range(min(y), max(y)+1))
plt.yticks(range(0, 30))

# 添加XY轴和图表描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位（摄氏度）")
plt.title("10-12点每分钟气温变化情况")

# 保存图片
# plt.savefig('./temp/t1.svg')
# 展示图片
plt.show()




