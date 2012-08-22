class Party(object):
    
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation


class Candidate(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.votes = 0


class Race(object):
    
    def __init__(self, title, jurisdiction):
        self.title = title
        self.jurisdiction = jurisdiction
        self.candidates = []
        self.total_votes = 0

class DataSource(object):
    """
    Object to define what each data source will return.

    @args:
    source\tA string representing the source type.
    """
    
    def __init__(self):
        self.source = ''
        self.href = ''
        self.colums = {}
        self.races = {}

