import random

class Permutation:
    def __init__(self, line: str) -> None:
        self.line: str = line + ' '

    def colum(self) -> list:
        line: list = self.line.split(' ')
        number_colum: int = len(line[0]) # Кол-во столбцов определяется по длине первого слова
        
        # Определяем ключи
        keys: list = []
        while True:
            x = 0
            number: int = random.randint(1, number_colum)

            for i in keys:
                if number == i:
                    x = 1
                    break

            if x != 1:
                keys.append(number)

            if len(keys) == number_colum:
                break
        
        return keys, number_colum

    def permutation(self) -> None:
        mass: list = []
        colum: list = self.colum()
        keys: list = colum[0]
        number_colum: int = colum[1]
        number_line: int = len(self.line)

        # Определяем количество строк
        if number_line % number_colum > 0:
            number_list: int = int(number_line / number_colum) + 1
        else:
            number_list: int = int(number_line / number_colum)

        for i in range(number_list):
            mass.append([])

        # Заполнения массива
        y = 0
        x = 1
        for i in self.line.split(' '):
            for a in i + ' ':
                mass[y].append(a)

                if x == number_colum:
                    y += 1
                    x = 0

                x += 1
        
        # Добавляем не достающие элементы
        len_mass = len(mass[len(mass) - 1])
        if len_mass != number_list:
            for i in range(number_colum - len_mass):
                mass[len(mass) - 1].append(' ')

        print(f'Открытй текст: {self.line}')
        print(f'Ключи: {keys}')
        print(f'Сдвиг: {len(keys)}')

        for i in mass:
            print(i)

        respons = ''
        for i in range(1, len(keys) + 1):
            x = 0

            # Находим столбец
            for a in keys:
                if a == i:
                    break
                x += 1
            
            for u in mass:
                respons += u[x]

        print(f'Закрытый текст: {respons}')

# Permutation('широкое распространение получила разновидность').permutation()

class DePermutation:
    def __init__(self, shift: str, line: str, keys: list) -> None:
        self.shift: str = shift
        self.line = line
        self.keys: list = keys

    def depermutation(self) -> list:
        line: list = []
        x: int = 0
        y: int = -1
        for i in self.shift:
            if x == 0:
                line.append([])
                y += 1
            
            line[y].append(i)

            x += 1
            if x == 7:
                x = 0

        number_line: int = len(line)
        line_2: list = []
        for i in range(number_line):
            line_2.append([])
        
        
        for i in self.keys:
            i -= 1
            y = 0
            for u in line_2:
                u.append(line[i][y])
                y += 1

        respons: str = ''
        for i in line_2:
            for u in i:
                respons += u

        print(f'Кодированный текст: {self.shift}')
        print(f'Ключи: {self.keys}')
        print(f'Сдвиг: {len(self.keys)}')
        for i in line_2:
            print(i)
        print(f'Декодированный текст: {respons}')

# DePermutation('кпно и ш сичзорар лоторелрд еонуан осапавьиртеинс', 7, [2, 7, 3, 6, 1, 4, 5]).depermutation()