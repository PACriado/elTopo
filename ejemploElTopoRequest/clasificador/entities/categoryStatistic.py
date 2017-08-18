

class categoryStatistic():

    def __init__(self, Category, Statistic):
        self.category=Category
        self.statistic=Statistic

    def setcategory(self, Category):
        self.category = Category

    def getcategory(self):
        return self.category

    def setstatistic(self, Statistic):
        self.statistic = Statistic

    def getstatistic(self):
        return self.statistic
