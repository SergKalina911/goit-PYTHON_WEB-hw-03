from multiprocessing import Pool, cpu_count
import time

def factorize_number(n: int) -> list[int]:
    """ Факторизація одного числа """
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def factorize_sync(*numbers):
    """ Факторизація чисел у синхронному режимі """
    return [factorize_number(n) for n in numbers]

def factorize_parallel(*numbers):
    """ Факторизація чисел у паралельному режимі """
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_number, numbers)

if __name__ == "__main__":
    # Тестові числа для факторизації
    numbers = (128, 255, 99999, 10651060)
    
    # Вимірювання часу для синхронної факторизації
    start = time.time()
    sync_result = factorize_sync(*numbers)
    print("Час синхронного виконання:", time.time() - start, "сек")

    # Вимірювання часу для паралельної факторизації
    start = time.time()
    parallel_result = factorize_parallel(*numbers)
    print("Час паралельного виконання:", time.time() - start, "сек")

    # Перевірка
    a, b, c, d = sync_result
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]
    
    assert sync_result == parallel_result
    if True:
        print("Перевірка пройдена успішно!")
    