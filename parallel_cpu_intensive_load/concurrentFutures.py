import concurrent.futures
import time
import numpy as np


def write_job(arr, index):
    print("init",index)
    for i in range(len(arr[index])):
        arr[index][i] = i
    read_job(arr, index)
    print("done",index)


def read_job(arr, index):
    count = 0
    for i in range(len(arr[index])):
        if i % 2 == 0:
            count += 1
        else:
            count -= 1


def run_with_pool(array_len, array_children_len): 
    arr = np.zeros((array_len, array_children_len), dtype=int)
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(write_job, arr, i)
                   for i in range(array_len)]
        concurrent.futures.wait(futures)

    end = time.time()
    duration_ms = (end - start) * 1000
    print(f"Execution time: {duration_ms:.2f} milliseconds")


def main():
    array_len = 10
    array_children_len = int(1e8)
    run_with_pool(array_len, array_children_len)


if __name__ == "__main__":
    main()
