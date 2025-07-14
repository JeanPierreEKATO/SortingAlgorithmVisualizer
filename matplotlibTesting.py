import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Zufällige Liste erzeugen
data = []
i = 0
for i in range(100):
    data.append(i)

random.shuffle(data)

fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor('black')
bar_rects = ax.bar(range(len(data)), data, align="edge", color='green')
ax.set_title("Bubble Sort Visualisierung")
ax.set_xlim(0, len(data))
ax.set_ylim(0, max(data) + 10)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes, color='white')

iteration = [0]

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data

def update_fig(data, rects, iteration):
    for rect, val in zip(rects, data):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"Schritte: {iteration[0]}")

animator = animation.FuncAnimation(
    fig,
    func=update_fig,
    fargs=(bar_rects, iteration),
    frames=bubble_sort(data.copy()),
    interval=100,
    repeat=False
)

plt.show()
