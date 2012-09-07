import json

from utils import slugify, party_lookup, candidate_percentages

class Candidate(object):

    def __init__(self, name, party, votes, candidate_percentage):
        self.name = name
        self.party = party_lookup(party)
        self.votes = votes
        self.candidate_percentage = candidate_percentages(candidate_percentage)

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
        fileName = self.source
        for i in self.races.iteritems():
            race = i[1]
            if len(race.candidates) >1:
                candidates = []
                for c in race.candidates:
                    candidates.append(
                        {
                            'name': c.name,
                            'votes': c.votes,
                            'party': c.party,
                            'percentage': c.candidate_percentage
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
        allJson = json.dumps(dump, indent=4)
        print allJson
        jsonDump = open('../data/'+fileName+'.json', 'w+')
        jsonDump.write(allJson)
        jsonDump.close()    
   
   
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

