import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()
    return all_data

file_names = [f'./file {number}.txt' for number in range(1, 5)]

"""start_time = time.time()
for file_name in file_names:
    read_info(file_name)
end_time = time.time()
print("Время линейного выполнения:", end_time - start_time, "секунд")"""

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    print("Время многопроцессного выполнения:", end_time - start_time, "секунд")