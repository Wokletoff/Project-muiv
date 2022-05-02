class Global_Settings:
    def __init__(self):
        self._int_map = 3

    @property
    def int_map(self):
        return self._int_map
    @int_map.setter
    def int_map(self, value):
        self._int_map = value

settings = Global_Settings()