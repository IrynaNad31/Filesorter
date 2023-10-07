import multiprocessing
import time

def factorize_parallel(numbers):
    def worker(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.map(worker, numbers)
    return result


numbers = [12, 15, 28, 32]
start_time = time.time()
result_parallel = factorize_parallel(numbers)
end_time = time.time()
print("Паралельна версія:", result_parallel)
print("Час виконання (паралельно):", end_time - start_time, "секунд")
