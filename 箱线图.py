# import matplotlib.pyplot as plt
# import numpy as np
#
# # 假设数据，您需要根据实际情况替换这些数据
# # 这里我们使用随机数据来模拟箱线图的数据
# np.random.seed(0)
# data_without_avatar = [np.random.normal(50, 10, 100) for _ in range(7)]
# # data_with_avatar = np.random.normal(60, 15, 100)
#
# # 将数据分组，例如按不同的维度分组
# categories = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration', 'Overall']
# data = data_without_avatar
#
# # 绘制箱线图
# plt.figure(figsize=(10, 6))
# plt.boxplot(data, labels=categories)
#
# # 添加标题和标签
# plt.title('TLX Scores of Image Transcription')
# plt.xlabel('Category')
# plt.ylabel('Score')
#
# # 显示图形
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)
#
# fig, axs = plt.subplots(2, 2)
# fig.suptitle('2x2 ')
# axs[0, 0].plot(x, y)
# axs[0, 1].scatter(x, y, color='r')
# axs[1, 0].plot(x, -y, color='g')
# axs[1, 1].scatter(x, -y, color='m')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2, 2, gridspec_kw={'hspace': 0.5, 'wspace': 0.5})
fig.suptitle('2x2 子图示例（增加间距）')
axs[0, 0].plot(x, y)
axs[0, 1].scatter(x, y, color='r')
axs[1, 0].plot(x, -y, color='g')
axs[1, 1].scatter(x, -y, color='m')
plt.show()