import json

from elections.utils import slugify

class Party(object):
    
    def __init__(self, name, abbreviation):
        self.name = name
        self.slug = slugify(name)
        self.abbreviation = abbreviation


class Candidate(object):

    def __init__(self, first_name, last_name, votes):
        self.first_name = first_name
        self.last_name = last_name
        self.slug = slugify(first_name + last_name)
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
                        'first_name': c.first_name,
                        'last_name': c.last_name,
                        'votes': c.votes,
                    }
                )
            races.append(
                {
                    'name': race.title,
                    'total_votes': race.total_votes,
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

