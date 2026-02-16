import argparse
import random
import time
from .sorting_algorithms import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quicksort_first_pivot,
    quicksort_random_pivot
)



ALGORITHMS = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick_first": quicksort_first_pivot,
    "quick_random": quicksort_random_pivot
}



def generate_data(size, input_type):
    if input_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif input_type == "sorted":
        return list(range(size))
    elif input_type == "nearly_sorted":
        data = list(range(size))
        swaps = max(1, size // 20)  # 5% disorder
        for _ in range(swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            data[i], data[j] = data[j], data[i]
        return data
    else:
        raise ValueError("Unsupported input type")


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start


def run_single_benchmark(algorithm_name, size, trials, input_type):
    if algorithm_name not in ALGORITHMS:
        raise ValueError("Unsupported algorithm")

    algorithm = ALGORITHMS[algorithm_name]
    times = []

    for _ in range(trials):
        data = generate_data(size, input_type)
        times.append(measure_time(algorithm, data))

    avg_time = sum(times) / len(times)

    print("\n--- Single Benchmark Result ---")
    print(f"Algorithm : {algorithm_name}")
    print(f"Input Type: {input_type}")
    print(f"Size      : {size}")
    print(f"Trials    : {trials}")
    print(f"Avg Time  : {avg_time:.8f} seconds")


def run_multi_size_benchmark(algorithm_name, sizes, trials, input_type):
    if algorithm_name not in ALGORITHMS:
        raise ValueError("Unsupported algorithm")

    algorithm = ALGORITHMS[algorithm_name]

    print("\n--- Multi-Size Benchmark ---")
    print(f"Algorithm : {algorithm_name}")
    print(f"Input Type: {input_type}")
    print("\nSize\tAverage Time (s)")
    print("-" * 30)

    for size in sizes:
        times = []
        for _ in range(trials):
            data = generate_data(size, input_type)
            times.append(measure_time(algorithm, data))

        avg_time = sum(times) / len(times)
        print(f"{size}\t{avg_time:.8f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Algorithm Benchmark Tool")

    parser.add_argument("--algorithm", type=str, required=True,
                        help="Algorithm to benchmark: bubble, insertion, merge")

    parser.add_argument("--size", type=int,
                        help="Input size for single benchmark")

    parser.add_argument("--trials", type=int, default=10,
                        help="Number of trials to average")

    parser.add_argument("--input-type", type=str, default="random",
                        choices=["random", "sorted", "nearly_sorted"],
                        help="Type of input distribution")

    parser.add_argument("--multi", action="store_true",
                        help="Run benchmark across predefined sizes")

    args = parser.parse_args()

    if args.multi:
        sizes = [50, 100, 200, 300, 400]
        run_multi_size_benchmark(args.algorithm, sizes, args.trials, args.input_type)
    else:
        if args.size is None:
            raise ValueError("You must provide --size for single benchmark mode")
        run_single_benchmark(args.algorithm, args.size, args.trials, args.input_type)
