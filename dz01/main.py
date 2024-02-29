"""Дан лог сервера, который содержит логи операций с машинами. Для
идентификации машин используются IPv4 адреса.Нужно определить частоту
встречаемости IP адресов.
На вход программе лог – текстовый файл log.txt.
На выходе ожидается новый файл, содержащий список адресов с
количеством упоминаний адреса (список IP-адресов, отсортированных в порядке
убывания количества упоминаний). Если несколько IP-адресов имеют одинаковое
количество упоминаний, то к ним применяется сортировка строк по убыванию.
Важно:
 В логе может встречаться текст похожий на IP, но не являющимся им,
например, 0.0.0.1000
 В логах могут встречаться маски подсети, например 192.168.0.0/16. Их не
нужно считать как ip.
 Строки логов могут быть пустые.
 Строка лога не обязательно содержит ip, но в логах обязательно содержится
хотя бы один ip.
__________Решение___________"""
import re
ip = []
result1 = []
def get_ip_from_log(path) -> list:
    """
    Функция для обработки текстовых лог файлов.
    :param path: - на входе текстовый файл логов содержащий в себе айпи адреса.
    :return: List - список содержащий в себе IP адреса
    """
    with open(path, 'r', encoding='utf-8') as file:
        ip = file.read()
        global ip1
        ip1 = re.findall(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', ip)
        return ip1

def analyzing_ip(ip1: list) -> list:
    """Аналитическая функция, обрабатывает полученные данные.
    :param ip1: List - принимает список адресов ip1: list, обрабатывает его и сортирует.
    :return list - возвращает новый список ip2 с корректными адресами и количеством вхождений в первый список соответственно"""
    mistake = []
    ip2 = []
    save = []
    for k in ip1:
        save.append([int(i) for i in k.split('.')])
    for i in save:
        if i[0] > 255 or i[0] < 1:
            mistake.append(i)
        if i[1] > 255 or i[2] > 255:
            mistake.append(i)
        if i[3] > 255 or i[3] < 1:
            mistake.append(i)
    for i in save:
        if i not in mistake:
            a = ".".join(str(k) for k in i)
            ip2.append(a)
    result = {}
    if not ip2:
        raise Exception('В файле отсутствуют корректные ip адреса')
    for i in ip2:
        result[i] = result.get(i, 0) + 1
        global result1
    result1 = list(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result1

def processing_ip(result1: list) -> None:
    """Функция для записи результата в новый файл(file2), запись производиться в два столбца.
    :param result1: - функция принимает список
    :return: None - ничего не возвращает.
    """
    result2 = ''
    for i in result1:
        result2 += str(i[0] + '\t' + str(i[1])) + '\n'
    file2 = open('file2', 'w', encoding='utf-8')
    file2.write(result2)
    file2.close()


def main():
    try:
        get_ip_from_log('log.txt')
        analyzing_ip(ip1)
        processing_ip(result1)
    except Exception as e:
        print(e)
if __name__ == '__main__':
     main()
