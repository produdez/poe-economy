import pandas as pd
import numpy as np
from data_model import *

class DataHelper:
    str_type, float_type = str, np.float64
    CURRENCY_DATA_DTYPES = {
        'League' : str_type,
        'Get' : str_type,
        'Pay' : str_type,
        'Value' : float_type,
        'Confidence' : str_type
    }

    ITEM_DATA_DTYPES = {
        'League' : str_type,
        'Id' : str_type,
        'Type' : str_type,
        'Name' : str_type,
        'BaseType' : str_type,
        'Variant' : str_type,
        'Links' : str_type,
        'Value' : float_type,
        'Confidence' : str_type
    }

    PARSE_DATE = ['Date']

    @staticmethod
    def load_POE_data(data_path, league, league_specific_name, league_type):
        print(f'Load POE DATA, league specific name: {league_specific_name}, type: {league_type}')

        print('Reading currency!')
        currency = pd.read_csv(
            f'{data_path}/{league}/{league_specific_name}.currency.csv', 
            delimiter=';', 
            dtype=DataHelper.CURRENCY_DATA_DTYPES,
            parse_dates=DataHelper.PARSE_DATE
        )
        
        print('Reading items!')
        items = pd.read_csv(
            f'{data_path}/{league}/{league_specific_name}.items.csv', 
            delimiter=';', 
            dtype=DataHelper.ITEM_DATA_DTYPES,
            parse_dates=DataHelper.PARSE_DATE
        )

        return POEData(
            name = league_type,
            currency = currency,
            item = items
        )

    @staticmethod
    def load_league_data(data_path, league):
        print(f'Loading League Data, league: {league}')

        league_name_types = [
            (league, 'Event'),
            (f'Hardcore {league}', 'Event Hardcore'),
            ('Hardcore', 'Hardcore'),
            ('Standard', 'Standard')
        ]

        event, event_hc, hc, standard = [
            DataHelper.load_POE_data(data_path, league, specific_name, league_type) for specific_name, league_type in league_name_types
        ]
        return LeagueData(
            name = league,
            event_data= event,
            event_hardcore_data= event_hc,
            standard_hardcore_data= hc,
            standard_data= standard
        )

    @staticmethod
    def load_all_leagues_data(data_path, leagues):
        return_data = dict()
        for league in leagues:
            return_data[league] = DataHelper.load_league_data(data_path, league)
        return return_data

    @staticmethod
    def get_currency_data(name, data, league):
        df = data[league].event.currency
        return df[df['Get'] == name]
    
    @staticmethod
    def get_concatinated_currency_data(name, data, leagues = None):
        if not leagues: leagues = data.keys()
        merged_df = pd.concat(
            [DataHelper.get_currency_data(name, data, league) for league in leagues]
        ).reset_index(drop=True).sort_values('Date')
        return merged_df
