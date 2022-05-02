class Global_Settings:
    def __init__(self):
        self._charts = 1

    @property
    def charts(self):
        return self._charts
    @charts.setter
    def charts(self, value):
        self._charts = value

settings = Global_Settings()