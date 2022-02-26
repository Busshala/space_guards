class Statistics():
    """отслеживаем статистику
    """

    def __init__(self):
        """инициализация статистики
        """
        self.reseting()
        self.running = True

    def reseting(self):
        """сколько будет жизней у пушшшки
        """
        self.weapons_we_have = 2
        self.score = 0
