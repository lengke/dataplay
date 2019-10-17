from matplotlib import pyplot as plt


# 绘制条形图
figure = plt.figure(figsize=(14, 8), dpi=80)

a = ["战狼2", "速度与激情8", "西游伏魔篇", "变形金刚5:\n最后的骑士大哥哥", "生化危机6", "美丽心灵", "哪吒脑海", "流浪地球", "开心人"]

b = [56.01, 26.94, 94.17, 53.16, 12.96, 70.14, 44.67, 39.63, 59.58]


plt.bar(a, b, width=0.4)
plt.yticks(range(0,110,10))

plt.title("2017年前5大电影票房排行", fontsize=16)


plt.show()
