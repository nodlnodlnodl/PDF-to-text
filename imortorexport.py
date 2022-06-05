def whatiscountry(traectoriya):
    with open(traectoriya, 'r', encoding="utf-8") as fp:
        lines = fp.readlines()

    country = [
        "Австралия", "Австрия", "Азербайджан", "Аландские острова", "Албания", "Алжир", "Ангилья", "Англия", "Ангола",
        "Андора", "Аргентина ", " Армения", "Аруба", "Афганистан", "Багамские острова", "Бангладеш", "Барбадос", "Бахрейн",
        "Белиз", "Белоруссия", "Бельгия", "Бенин", "Бермуды", "Болгария", "Боливия", "Бонайре", "Босния и Герцеговина",
        "Ботсвана", "Бразилия", "Бруней", "Буве", "Буркина-Фасо", "Бурунди", "Бутан", "Вануату", "Ватикан",
        "Великобритания", "Венгрия", "Венесуэла", "Вьетнам", "Габон", "Гаити", "Гайана", "Гамбия", "Гана", "Гваделупа",
        "Гватемала", "Гвиана",
        "Гвинея", "Германия", "Гернси", "Гибралтар", "Гондурас", " Гонконг", "Гренада", "Гренландия", "Греция", "Грузия",
        "Гуам", "Дания", "Конго", "ДРК", "Джерси", "Джибути", "Доминика", "Доминиканская Республика", "Европейский Союз",
        "Египет", "Замбия", "Западная Саха", "Зимбабве", "Израиль", "Индия", "Индонезия", "Иордания", " Иран", "Ирландия",
        "Ирак", "Исландия", "Испания", "Италия", "Йемен", "Кабо-Верде", "Казахстан", "Каймановы острова", "Камбоджа",
        "Камбоджи", "Камерун", "Канада", "Катар", "Кения", "Кипр", "Киргизия", "Кирибати", "Китай", "Кокосовые острова",
        "Колумбия", "Коморы", "Косово", "Коста-Рика", " Куба", "Кувейт", "Кюрасао", "Лаос", "Латвия", "Лесото", "Либерия",
        "Ливан", "Литва", "Лихтенштейн", "Люксембург", "Маврикий", "Мавритания", "Мадагаскар", "Майотта", "Макао",
        "Македония", "Малави", "Малайзия", "Мали", "Мальдивы", "Мальта", "Марокко", "Мартиника", "Маршалловы Острова",
        "Мексика", " Микронезия", "Мозамбик", "Молдавия", "Монако", "Монголия", "Монтсеррат", "Мьянма", "Намибия", "Науру",
        "Непал", "Нигер", "Нигерия", "Нидерланды", "Никарагуа", "Ниуэ", "Новая Зеландия", "Новая Каледония", "Норвегия",
        "Норфолк", "Объединëнные Арабские Эмираты", "Объединенные Арабские Эмираты", "ОАЭ", "Оман", "Пакистан", "Палау",
        "Палестина", "Палестинские территории", "Панама", "Папуа-Новая Гвинея", "Новая Гвинея", "Папуа", "Гвинея",
        "Парагвай", "Перу", "Польша", "Португалия", "Пуэрто-Рико", "Республика Ирак", "Республика Конго", "Конго",
        "Реюньон", "Руанда", "Румыния", "Сальвадор", "Самоа", " Сан-Марино", "Саудовская Аравия", "Свазиленд",
        "Северная Корея", "КНДР", "Корейская Народно-Демократическая Республика", "Сейшельские острова", "Сейшелы",
        "Сен-Бартелеми", "Сен-Мартен", "Сенегал", "Сербия", "Сингапур", "Синт-Мартен", "Сирия",
        "Сирийская Арабская Республика", "САР", "Словакия", "Словения", "Соломоновы Острова", "Сомали", "СССР", "Судан",
        "Суринам", "США", "Соединëнные Штаты Америки", "Соединенные Штаты Америки", "Америка", "Таджикистан", "Таиланд",
        "Китайская Республика Тайвань", "Тайвань", "Танзания", "Китайская Республика", "Того", "Тонга", "Токелау", "Тувалу",
        "Тунис", "Туркмения", "Турция", "Уганда", " Узбекистан", "Украина", "Уругвай", "Уэльс", "Фарерские острова",
        "Фиджи", "Филиппины", "Финляндия", "Фолклендские острова", "Франция", "Хорватия",
        "Центральноафриканская Республика", "Чад",
        "Черногория", "Чехия", "Чили", "Швейцария", "Швеция", "Шотландия", "Шри-Ланка", "Шпицберген",
        "Шпицберген и Ян-Майен", "Ян-Майен", "Эквадор", "Экваториальная Гвинея", "Эритрея", "Эстония", "Эфиопия", "ЮАР",
        "Южно-Африканская Республика", "Южная Корея", "Южный Судан", "Ямайка", "Япония"]
    imp = 0
    for z in range(len(country)):
        for i in range(len(lines)):
            if lines[i].find(country[z]) != -1:
                return ('Импортный продукт, ' + country[z])
                imp += 1
                break
    if imp == 0:
        return "Отчественный продукт"
    fp.close()

def foundnumber(traectoriya):
    with open(traectoriya, 'r', encoding="utf-8") as fp:
        lines = fp.readlines()
    arr = lines[1].split(sep=" ")
    return (arr[4])
    fp.close()

def foundname(sysnames):

    f = open(sysnames, 'r', encoding='utf-8')
    start = 'ОПИСАНИЕ ТИПА СРЕДСТВА ИЗМЕРЕНИЙ'
    end = 'Назначение средства измерений'
    startFound = False
    strfull = ""
    for l in f:
        str = l.strip()
        if not str:
            continue
        if end in str:
            break
        if startFound:
            strfull = strfull + str + " "
        if start in str:
            startFound = True
    return strfull
    f.close()