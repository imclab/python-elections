import json

from utils import slugify

class Candidate(object):

    def __init__(self, first_name, last_name, party, votes):
        self.first_name = first_name
        self.last_name = last_name
        self.slug = slugify(first_name + last_name)
        self.party = party
        self.votes = votes

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        # TODO
        return self.__unicode__()


class Race(object):
    
    def __init__(self, title, jurisdiction, total_votes):
        self.title = title
        self.slug = slugify(title)
        self.jurisdiction = jurisdiction
        self.candidates = []
        self.total_votes = total_votes

    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    
    def __unicode__(self):
        return "%s" % self.title

    def __repr__(self):
        # TODO
        return self.__unicode__()


class DataSource(object):
    """
    Object to define what each data source will return.

    @args:
    source    A string representing the source type.
    """
    
    def __init__(self):
        self.source = ''
        self.races = {}

    def get_results(self):
        # This should be defined by the subclass
        raise NotImplementedError

    def get_or_create_race(self, race):
        try:
            self.races[race.slug]
            created = False
        except KeyError:
            self.races[race.slug] = race
            created = True
        return self.races[race.slug], created 

    def json_dump_results(self):
        races = []
        for i in self.races.iteritems():
            race = i[1]
            candidates = []
            for c in race.candidates:
                candidates.append(
                    {
                        
                        'last_name': c.last_name,
                        'votes': c.votes,
                        'party': c.party,
                        'first_name': c.first_name,
                    }
                )
            races.append(
                {
                    'total_votes': race.total_votes,         
                    'name': race.title, 
                    'candidates': candidates, 
                }
            )

        dump = {
            'races': races
        }
        print json.dumps(dump, indent=4)

    def print_results(self):
        for i in self.races.iteritems():
            race = i[1]
            print ''
            print race
            for c in race.candidates:
                print c
                print c.votes
                print ''
            print ''

