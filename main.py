import random
import time

from algos.crc_mirrored import crc_mirrored
from algos.crc_mirrored_table_algorithm import create_mirrored_crc_table, crc_mirrored_table_algorithm
from algos.crc_serial import crc_serial
from algos.crc_table_algorithm import crc_table_algorithm
from algos.utils.create_crc_table import create_crc_table

from tabulate import tabulate
# Параметри для CRC-4-ITU
message_length = 1000
polynomial = 0b10011
polynomial_length = 4


def main():
    message = [random.choice([0, 1]) for _ in range(message_length)]

    # Виконання простого послідовного алгоритму і вимірювання часу
    start_time = time.time()
    crc_serial_result = crc_serial(message, polynomial, polynomial_length)
    serial_time = time.time() - start_time

    # Створення таблиці CRC для CRC-4-ITU
    crc_table = create_crc_table(polynomial, polynomial_length)

    # Виконання табличного алгоритму і вимірювання часу
    start_time = time.time()
    crc_table_result = crc_table_algorithm(message, crc_table, polynomial_length)
    table_time = time.time() - start_time

    # Виконання дзеркального алгоритму і вимірювання часу
    start_time = time.time()
    crc_mirrored_result = crc_mirrored(message, polynomial, polynomial_length)
    mirrored_time = time.time() - start_time

    # Створення дзеркальної таблиці CRC
    mirrored_crc_table = create_mirrored_crc_table(polynomial, polynomial_length)

    # Виконання дзеркального табличного алгоритму і вимірювання часу
    start_time = time.time()
    crc_mirrored_table_result = crc_mirrored_table_algorithm(message, mirrored_crc_table, polynomial_length)
    mirrored_table_time = time.time() - start_time

    table = [
        ["Serial", crc_serial_result, serial_time],
        ["Table", crc_table_result, table_time],
        ["Mirrored", crc_mirrored_result, mirrored_time],
        ["Mirrored Table", crc_mirrored_table_result, mirrored_table_time],
    ]

    print(tabulate(table, headers=["Algorithm", "CRC", "Time"]))


if __name__ == "__main__":
    main()



