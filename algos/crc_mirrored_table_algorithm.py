# Створення дзеркальної таблиці для CRC-4-ITU
from algos.utils.reverse_bits import reverse_bits


def create_mirrored_crc_table(polynomial, polynomial_length):
    table = []
    for byte in range(256):  # для кожного можливого значення байта (256 комбінацій)
        crc = reverse_bits(byte, 8) >> (8 - polynomial_length - 1)  # перевертаємо байт і обрізаємо до полінома
        for _ in range(8):  # обробка кожного біта
            if crc & 1:  # якщо молодший біт дорівнює 1
                crc = (crc >> 1) ^ reverse_bits(polynomial, polynomial_length + 1)
            else:
                crc >>= 1
        # Дзеркально перевертаємо результат і зберігаємо
        table.append(reverse_bits(crc, polynomial_length) & ((1 << polynomial_length) - 1))
    return table

# Дзеркальний табличний алгоритм для CRC-4-ITU
def crc_mirrored_table_algorithm(message, crc_table, polynomial_length):
    crc = 0
    for bit in message:
        # Вираховуємо індекс для таблиці з урахуванням поточного стану CRC і нового біта
        top = (crc ^ bit) & ((1 << polynomial_length) - 1)
        crc = (crc >> 1) ^ crc_table[top]
    return crc & ((1 << polynomial_length) - 1)