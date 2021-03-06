from model.group import Group
import string
import random
import os.path
import jsonpickle
#библиотека для чтения опций командной строки
import getopt
#библиотека для использования опций командной строки
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

#указывыем значения параметров: количество генерируемых циклов,путь к файлу, в который будут записаны данные
n = 5
f = "data/groups.json"

#  кортеж из названий переменных и значения, для вврдимых опций проверяются n и f для использования нижепо коду
for o, a in opts:
    if a == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix+"".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("name",10),group_header=random_string("header",20), group_footer=random_string("footer", 13))
    for i in range(n)]


#склейка родительской директории текущего файла и названия файла, в который будут записаны тестовые данные, вложенная функция определяет абсолютный путь к текущему файлу
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

#открываем файл для записи по пути path для записи в него сгенерированных данных
with open(path, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
# параметр indent для переноса объектов списка в отдельные строки
    out.write(jsonpickle.encode(testdata))
