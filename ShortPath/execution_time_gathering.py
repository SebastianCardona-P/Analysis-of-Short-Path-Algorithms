import time
from ShortPath import Graph
from ShortPath import constants
from ShortPath import data_generator

def take_execution_time(step, samples_by_size, minimum_vertex=constants.MIM_NUM_VERTEX,
                        maximum_vertex=constants.MAX_NUM_VERTEX):
    return_table = []

    for size in range(minimum_vertex, maximum_vertex + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table

"""
    It will return 3 values, one per algorithm: The execution time
"""


def take_times(size, samples_by_size):
    samples = [
        data_generator.get_graph(size) for _ in range(samples_by_size)
    ]

    return [
        take_time_for_algorithm(samples, "dijkstra"),
        take_time_for_algorithm(samples, "floyd_warshall"),
        take_time_for_algorithm(samples, "bellman_ford"),
    ]

"""
    Returns the median of the execution time
"""


def take_time_for_algorithm(samples, algorithm):
    times = []

    if algorithm == "dijkstra":
        for sample in samples:
            start = time.time()
            sample.dijkstra(sample.vertexes[0])
            end = time.time()
            times.append(constants.TIME_MULTIPLIER * (end - start))
    elif algorithm == "floyd_warshall":
        for sample in samples:
            start = time.time()
            sample.floyd_warshall()
            end = time.time()
            times.append(constants.TIME_MULTIPLIER * (end - start))
    elif algorithm == "bellman_ford":
        for sample in samples:
            start = time.time()
            sample.bellman_ford(sample.vertexes[0])
            end = time.time()
            times.append(constants.TIME_MULTIPLIER * (end - start))

    times.sort()
    return times[len(times) // 2]
