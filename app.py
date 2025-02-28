import matplotlib.pyplot as plt
import numpy as np
from ShortPath import execution_time_gathering

if __name__ == "__main__":
    step = 100
    samples_by_size = 2

    sizes = []
    dijkstra_times = []
    floyd_times = []
    bellman_times = []

    table = execution_time_gathering.take_execution_time(
        step, samples_by_size
    )
    print("Size | Dijkstra | Floyd-Warshall | Bellman-Ford")
    for row in table:
        print(row)
        sizes.append(row[0])  # Graph size
        dijkstra_times.append(row[1])  # Dijkstra time
        floyd_times.append(row[2])  # Floyd-Warshall time
        bellman_times.append(row[3])  # Bellman-Ford time

    plt.figure(figsize=(10, 6))

    plt.plot(sizes, dijkstra_times, marker='o', linestyle='-', label='Dijkstra', color='blue')
    plt.plot(sizes, floyd_times, marker='s', linestyle='--', label='Floyd-Warshall', color='red')
    plt.plot(sizes, bellman_times, marker='^', linestyle='-.', label='Bellman-Ford', color='green')

    plt.xlabel('Graph Size')
    plt.ylabel('Execution time (ns)')
    plt.title('Time comparison between shortest path algorithms')
    plt.legend()
    plt.grid()

    plt.show()

    x = np.arange(len(sizes))
    width = 0.3  # bar width

    plt.subplot(1, 2, 2)  # second
    plt.bar(x - width, dijkstra_times, width=width, label='Dijkstra', color='blue')
    plt.bar(x, floyd_times, width=width, label='Floyd-Warshall', color='red')
    plt.bar(x + width, bellman_times, width=width, label='Bellman-Ford', color='green')
    plt.xlabel('Graph Size')
    plt.ylabel('Execution time (ns)')
    plt.xticks(ticks=x, labels=sizes)
    plt.title('Execution Time Comparison (Bar Chart)')
    plt.legend()
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()

