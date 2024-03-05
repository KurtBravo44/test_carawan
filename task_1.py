def order(n) -> int:
    """
    выводит n первых элементов последовательности
    (число повторяется столько раз, чему оно равно)
    """

    result = ''
    for i in range(1, n+1):
        str_num = str(i)
        result += str_num * i
    return int(result)

print(order(5))