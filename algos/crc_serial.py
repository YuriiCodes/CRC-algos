# Функція для простого послідовного алгоритму CRC-4-ITU
def crc_serial(message, polynomial, polynomial_length):
    # Доповнюємо повідомлення нулями зліва для процесу обчислення CRC
    padded_message = message + [0] * polynomial_length
    crc = 0

    for bit in padded_message:
        # Зсув вліво і додаємо поточний біт
        crc = ((crc << 1) | bit) & ((1 << (polynomial_length + 1)) - 1)
        if crc & (1 << polynomial_length):  # якщо старший біт дорівнює 1
            crc ^= polynomial

    # Повертаємо результат CRC, видаляючи зайві біти
    return crc & ((1 << polynomial_length) - 1)