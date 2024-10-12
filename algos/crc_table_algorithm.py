# Табличний алгоритм для CRC-4-ITU
def crc_table_algorithm(message, crc_table, polynomial_length):
    crc = 0
    for bit in message:
        # Вираховуємо індекс для таблиці з урахуванням поточного стану CRC і нового біта
        top = (crc >> polynomial_length) ^ bit
        crc = ((crc << 1) & ((1 << (polynomial_length + 1)) - 1)) ^ crc_table[top]
    return crc & ((1 << polynomial_length) - 1)