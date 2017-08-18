

class categoryStatistic():

    def __init__(self, Category, Statistic,URL=""):
        self.url=URL
        self.category=Category
        self.statistic=Statistic

    def seturl(self, URL):
        self.url = URL

    def geturl(self):
        return self.url

    def setcategory(self, Category):
        self.category = Category

    def getcategory(self):
        return self.category

    def setstatistic(self, Statistic):
        self.statistic = Statistic

    def getstatistic(self):
        return self.statistic
