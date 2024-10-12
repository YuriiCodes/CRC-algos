# Створення таблиці залишків для табличного алгоритму CRC-4-ITU
def create_crc_table(polynomial, polynomial_length):
    table = []
    for byte in range(256):  # для кожного можливого значення байта (256 комбінацій)
        crc = byte
        for _ in range(8):  # обробка кожного біта в байті
            if crc & (1 << (polynomial_length + 3)):  # перевірка старшого біта (7+1 для полінома 4-го порядку)
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
        # Зберігаємо лише останні 4 біти
        table.append(crc & ((1 << (polynomial_length + 1)) - 1))
    return table