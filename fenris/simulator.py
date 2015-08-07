import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
fig.set_dpi(100)
fig.clear()

ax = plt.axes(xlim=(-600, 250), ylim=(-250, 250))
ax.set_autoscaley_on(True)

myline = plt.Line2D([], [], color='g', lw=1)

myline1 = plt.Line2D([], [], color='b', lw=2,
                     marker='.',
                     markersize=15,
                     markerfacecolor='r',
                     markeredgecolor='r')

myline2 = plt.Line2D([], [], color='b', lw=2,
                     marker='.',
                     markersize=15,
                     markerfacecolor='r',
                     markeredgecolor='r')

myline3 = plt.Line2D([], [], color='dodgerblue', lw=2,
                     marker='.',
                     markersize=15,
                     markerfacecolor='r',
                     markeredgecolor='r')

myline4 = plt.Line2D([], [], color='dodgerblue', lw=2,
                     marker='.',
                     markersize=15,
                     markerfacecolor='r',
                     markeredgecolor='r')

angle = np.arange(0, 2 * math.pi, 0.1)
angle2 = np.arange(-math.pi, math.pi, 0.1)
x = 200*np.cos(angle)
y = map(lambda x: x if x > 0 else 0, 100*np.sin(angle))
line = plt.Line2D(x, y, lw=1, color='r')

x = [_x-300 for _x in 200*np.cos(angle)]
y = map(lambda x: x if x > 0 else 0, 100*np.sin(angle))
line2 = plt.Line2D(x, y, lw=1, color='r')


def leg_position(d, angle):
    _angle = np.arccos((d/2)/150)
    _a = -150*np.sin(_angle)
    x = _a*np.cos(angle)
    y = _a*np.sin(angle)
    return x, y


def init():
    ax.add_line(myline)
    ax.add_line(myline1)
    ax.add_line(myline2)
    ax.add_line(line)
    ax.add_line(myline3)
    ax.add_line(myline4)
    ax.add_line(line2)
    return myline, myline1, myline2, line, line2, myline3, myline4


def animate(i):
    x = 200*np.cos(angle[i])
    y = 100*np.sin(angle[i])
    y = y if y > 0 else 0

    myline.set_data([0, x], [200, y])
    _dist = np.sqrt(x**2+(200-y)**2)
    _angle = np.arcsin(x/_dist)
    lx, ly = leg_position(_dist, _angle)
    myline1.set_data([0, x/2 + lx], [200, (200+y)/2 + ly])
    myline2.set_data([x/2 + lx, x], [(200+y)/2 + ly, y])

    x = 200*np.cos(angle2[i])
    y = 100*np.sin(angle2[i])
    y = y if y > 0 else 0
    _dist = np.sqrt(x**2+(200-y)**2)
    _angle = np.arcsin(x/_dist)
    lx, ly = leg_position(_dist, _angle)
    myline3.set_data([-300, x/2 + lx - 300], [200, (200+y)/2 + ly])
    myline4.set_data([x/2 + lx - 300, -300+x], [(200+y)/2 + ly, y])

    return myline, myline1, myline2, line, line2, myline3, myline4


ani = animation.FuncAnimation(fig,
                              animate,
                              np.arange(0, 63, 1),
                              init_func=init,
                              interval=1)
plt.axis('scaled')
plt.axis([-600, 250, -100, 250])
plt.show()
