import pandas as pd


'''
This is our data structure for simple ordering of the data
'''
class POEData:
    def __init__(self, name: str,currency: pd.DataFrame, item: pd.DataFrame) -> None:
        self.name = name
        self.item = item
        self.currency = currency
    def stats(self):
        return f'DataName: {self.name}, Shapes: item-{self.item.shape}, currency-{self.currency.shape}'

class LeagueData:
    def __init__(self, name: str, event_data: POEData, event_hardcore_data: POEData, standard_data: POEData, standard_hardcore_data: POEData) -> None:
        self.name = name
        self.event = event_data
        self.event_hardcore = event_hardcore_data
        self.standard = standard_data
        self.standard_hardcore = standard_hardcore_data

    def all_data(self): return [self.event, self.event_hardcore, self.standard, self.standard_hardcore]

    def stats(self):
        data_stats = "\n\t".join([poe_data.stats() for poe_data in self.all_data()])
        return f'''
League: {self.name}
Data Stats:
    {data_stats}
        '''
    def __str__(self) -> str:
        return self.stats()