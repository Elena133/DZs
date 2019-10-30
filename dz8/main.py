import figures

figuresList = []

for i in range(3):
    choice = input("Круг(к), прямоугольник(п) или треугольник(т): ")

    if choice == 'к':
        figure = figures.Circle(float(input("Радиус: ")))

    elif choice == 'п':
        l = float(input("Длина: "))
        w = float(input("Ширина: "))

        figure = figures.Rectangle(w, l)

    elif choice == 'т':
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        c = float(input("Третья сторона: "))

        figure = figures.Triangle(a, b, c)

    figuresList.append(figure)

choice = input("Максимальная площадь (пл)б максимальный периметр(пр): ")
if choice == 'пл':
    maxS = 0
    n = ''
    fun = 'Максимальная площадь у '
    for i in figuresList:
        s = i.getSquare()
        if maxS < s:
            maxS = s
            n = i.name

elif choice == 'пр':
    maxS = 0
    n = ''
    fun = 'Максимальный периметр у '
    for i in figuresList:
        s = i.getPer()
        if maxS < s:
            maxS = s
            n = i.name

print(fun, n, ':', maxS)
