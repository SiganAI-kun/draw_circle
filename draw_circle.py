import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes()
ax.set_aspect('equal')
# 半径の設定
radius1 = 10
radius2 = 5
# 描画する円の定義
c1 =  patches.Circle(xy=(0, 0), radius=radius1, fc='black', zorder=1)
c2 =  patches.Circle(xy=(0, 0), radius=radius2, fc='red', zorder=2)
# 円の描画
ax.add_patch(c1)
ax.add_patch(c2)

plt.xlim(-15, 15)
plt.ylim(-15, 15)

plt.savefig('double_circle.png')
# plt.show()