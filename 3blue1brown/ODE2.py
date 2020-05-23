"""
key 'python ODE2.py' to run
start from here "3blue1brown"
"https://www.youtube.com/watch?v=ly4S0oi3Yz8"
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update_arr(arr, rate=1):  # rate(0~1)
    df = np.diff(arr)
    df_f = np.hstack((0, -df))
    df_r = np.hstack((df, 0))
    dff = (df_f + df_r) / 2
    arr += dff * rate


n = 100
x = np.arange(n)
arr = np.hstack((np.ones(shape=(n // 2)), np.zeros(n // 2)))
# arr = np.sin(np.linspace(0, 3 * np.pi, n, endpoint=False))
# arr = np.linspace(0, 5, n)
max_val, min_val = arr.max(), arr.min()

fig, ax = plt.subplots(figsize=(8, 5))
p, = ax.plot(arr)


def init():
    ax.set_ylim(min_val - 0.1, max_val + 0.1)


def update_frame(frame):
    for i in range(5):
        update_arr(arr, 0.75)
    p.set_data(x, arr)


ani = FuncAnimation(fig=fig, func=update_frame, frames=1,
                    init_func=init, interval=15, blit=False)  # fps=50
plt.show()
