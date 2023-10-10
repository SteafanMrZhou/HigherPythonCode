import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i * number


start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(evaluate_item, item) for item in number_list]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
print("Thread pool execution in " + str(time.time() - start_time), "seconds")



# start_time = time.time()
# for item in number_list:
#     print(evaluate_item(item))
# print("Sequential execution in " + str(time.time() - start_time), "seconds")
