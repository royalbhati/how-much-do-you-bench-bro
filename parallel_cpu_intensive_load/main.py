import multiprocessing
import time
import numpy as np
import cProfile


def write_job(index):
    for i in range(len(arr[index])):
        arr[index][i] = i 
    read_job(arr, index)



def read_job(arr, index):
    count = 0
    for i in range(len(arr[index])):
        if i % 2 == 0:
            count += 1
        else:
            count -= 1


def worker_init(arr_):
    global arr
    arr = arr_


def run_with_pool(array_len, array_children_len):
    shared_array = multiprocessing.Array(
        'i', array_len * array_children_len, lock=False)
    arr = np.array(shared_array).reshape(
        array_len, array_children_len)

    start = time.time()
    print("start")
    with multiprocessing.Pool(initializer=worker_init, initargs=(arr,), processes=multiprocessing.cpu_count()) as pool:
        jobs = []
        for i in range(array_len):
            job = pool.apply_async(write_job, (i,))
            jobs.append(job)

        for job in jobs:
            job.get()

    end = time.time()
    duration_ms = (end - start) * 1000
    print("Execution time: %.2f milliseconds" % duration_ms)
 
# print(f"Execution time: {duration_ms:.2f} milliseconds")


def main():
     
    # profiler = cProfile.Profile()
    # profiler.enable()
    array_len = 10
    array_children_len = int(1e7)

    run_with_pool(array_len, array_children_len)

    # profiler.disable()
    # profiler.print_stats(sort='cumulative')


if __name__ == "__main__":
    main()
