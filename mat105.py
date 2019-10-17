from matplotlib import pyplot as plt

# 绘制散点图
figure = plt.figure(figsize=(20, 8), dpi=80)

# 北京2016年3,10月份每天白天的最高气温
march = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14,
		 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
		 23]

october = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23,
		   17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12,
		   13, 6]

# 为了让两个月的数据不重叠在一起，给他们设置不同的X轴范围
days_mar = range(1, 32)
days_oct = range(36, 67)
# 调整X轴的刻度
_x = list(days_mar) + (list(days_oct))

_xticks_list = [f"3月{i}日" for i in days_mar]
_xticks_list += [f"10月{i-35}日" for i in days_oct]
plt.xticks(_x, _xticks_list, rotation=270)

plt.xlabel("时间", fontsize=14)
plt.ylabel("温度(摄氏度)", fontsize=14)
plt.title("北京市2016年3月与10月白天最高温度散点图", fontsize=16)

plt.scatter(days_mar, march, label="三月气温")
plt.scatter(days_oct, october, label="十月气温")
plt.legend(loc="upper left", fontsize=14)
plt.show()
