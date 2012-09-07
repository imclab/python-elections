import csv
import re

import requests

from classes import Candidate, DataSource, Race

class SOS(DataSource):
    
    def __init__(self):
        self.source = 'SOS'
        self.href = 'http://vote.wa.gov/results/current/export/MediaResults.txt'
        self.columns = {
            'RaceID': 0,
            'RaceName': 1,
            'BallotID': 2,
            'BallotName': 3,
            'Votes': 4,
            'TotalBallotsCastByRace': 5,
            'PartyName': 6,
            'RaceJurisdictionTypeName': 7,
        }
        self.races = {}
        self.source = 'sos'

    def get_results(self):
        #r = requests.get('http://vote.wa.gov/results/current/export/MediaResults.txt')
        #data = r.text
        data = open('../data/example_sos_response.txt', 'r')

        reader = csv.reader(data, delimiter='\t')

        reader.next() # Skip header now
        for row in reader:
            candidate_name = row[self.columns['BallotName']]
            
            candidate_percentage = [row[self.columns['Votes']], row[self.columns['TotalBallotsCastByRace']]]
            raw_candidate_party = row[self.columns['PartyName']]
            party_regex = re.compile("Prefers (\w+) Party")
            party_result = party_regex.findall(raw_candidate_party)
            party_name = ''
            party_abbreviation = ''
            if party_result:
                party_name = party_result[0]
                party_abbreviation = party_name[0].upper()


            c = Candidate(
                candidate_name,
                party_name,
                row[self.columns['Votes']],
                candidate_percentage
            )

            r = Race(
                row[self.columns['RaceName']],
                row[self.columns['RaceJurisdictionTypeName']],
                row[self.columns['TotalBallotsCastByRace']]
            )

            race, created = self.get_or_create_race(r)
            race.add_candidate(c)
            
class KITSAP(DataSource):
    
    def __init__(self):
        self.source = 'SOS'
        self.href = 'http://vote.wa.gov/results/current/export/MediaResults.txt'
        self.columns = {
            'RaceID': 0,
            'RaceName': 13,
            'BallotID': 2,
            'BallotName': 14,
            'Votes': 3,
            'TotalBallotsCastByRace': 15,
        }
        self.races = {}
        self.source = 'Kitsap'

    def get_results(self):
        #r = requests.get('http://vote.wa.gov/results/current/export/MediaResults.txt')
        #data = r.text
        data = open('../data/Kitsap.txt', 'r')

        reader = csv.reader(data, delimiter='\t')

        reader.next() # Skip header now
        for row in reader:
            raw_candidate_name = row[self.columns['BallotName']]
            candidate_name_split = raw_candidate_name.split()
            candidate_first_name = candidate_name_split[0]
            candidate_last_name = ' '.join(candidate_name_split[1:])
            party_name = ''


            c = Candidate(
                candidate_first_name,
                candidate_last_name,
                party_name,
                row[self.columns['Votes']]
            )

            r = Race(
                row[self.columns['RaceName']],
                'Kitsap',
                row[self.columns['TotalBallotsCastByRace']]
            )

            race, created = self.get_or_create_race(r)
            race.add_candidate(c)

