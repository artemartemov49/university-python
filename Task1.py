def get_pharmacies():
    return (
        ("Аптека №1", "вул. Шевченка 10", "(044)123-45-67", 100000, 5000),
        ("Аптека №2", "вул. Пушкіна 20", "(044)234-56-78", 150000, 6000),
        ("Аптека №3", "вул. Лесі Українки 30", "(044)345-67-89", 80000, 4500),
        ("Аптека №4", "вул. Тарасівська 40", "(044)456-78-90", 120000, 5500),
        ("Аптека №5", "вул. Київська 50", "(044)567-89-01", 95000, 4800),
        ("Аптека №6", "вул. Гоголя 60", "(044)678-90-12", 110000, 5200),
        ("Аптека №7", "вул. Хрещатик 70", "(044)789-01-23", 135000, 1900)
    )


def pharmacies(tuples: tuple):
    avg_turnover = sum(value[3] for value in tuples) / len(tuples)
    avg_drugs = sum(value[4] for value in tuples) / len(tuples)
    biggest_pharmacies = [t for t in tuples if t[3] > avg_turnover and t[4] > avg_drugs]

    print("Середній товарообіг: " + str(avg_turnover))
    print("Cередня кількість препаратів: " + str(avg_drugs))
    print()
    print("Найбільші аптеки:")
    for item in biggest_pharmacies:
        print(str(item))


if __name__ == '__main__':
    rows = get_pharmacies()
    pharmacies(rows)
