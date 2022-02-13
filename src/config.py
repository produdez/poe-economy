import seaborn as sns

class Constants:
        LEAGUES = [
            'Essence',
            'Breach',
            'Legacy',
            'Harbinger',
            'Abyss',
            'Bestiary',
            'Incursion',
            'Delve',
            'Betrayal',
            'Synthesis',
            'Legion',
            'Blight',
            'Metamorph',
            'Delirium',
            'Harvest',
            'Heist',
            'Ritual',
            'Ultimatum',
            'Expedition',
        ]
        DATA_PATH = './data'
        REDUCED = False
        INTERESTING_CURRENCIES = [
            "Orb of Alteration",
            "Offering to the Goddess",
            "Vaal Orb",
            "Divine Orb",
            "Exalted Orb",
            "Chayula's Breachstone",
        ]
        IMG_OUTPUT_PATH = './images/output'
        DPI_OUTPUT = 300
        SAMPLE_LEAGUE_NAME = 'Delirium'

def setup():
    '''
    Needed setups
    '''
    sns.set(rc={'figure.figsize':(15,10)})
    print('Config finished!')