import multiprocessing
import time
import numpy as np

def write_job(arr, index):
    print("index init", index)
    for i in range(len(arr[index])):
        arr[index][i] = i

    print(len(arr[index]))
    read_job(arr, index)
    print("index done", index)


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
    with multiprocessing.Pool() as pool:
        jobs = []
        for i in range(array_len):
            job = pool.apply_async(write_job, (arr, i))
            jobs.append(job)

        for job in jobs:
            job.get()

    end = time.time()
    duration_ms = (end - start) * 1000
    print(f"Execution time: {duration_ms:.2f} milliseconds")


def main():

    num_cores = multiprocessing.cpu_count()
    print(f"Current number of CPU cores: {num_cores}")

    array_len = 10
    array_children_len = int(1e8)
    run_with_pool(array_len, array_children_len)


if __name__ == "__main__":
    main()

