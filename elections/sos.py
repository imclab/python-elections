# Data source:
# http://vote.wa.gov/results/current/export/MediaResults.txt

import csv
import re

import requests

from classes import Candidate, Party, Race

columns = {
    'RaceID': 0,
    'RaceName': 1,
    'BallotID': 2,
    'BallotName': 3,
    'Votes': 4,
    'TotalBallotsCastByRace': 5,
    'PartyName': 6,
    'RaceJurisdictionTypeName': 7,
}

races = {}

#r = requests.get('http://vote.wa.gov/results/current/export/MediaResults.txt')
#data = r.text
data = open('data/example_sos_response.txt', 'r')

reader = csv.reader(data, delimiter='\t')

reader.next() # Skip header now
for row in reader:
    raw_candidate_name = row[columns['BallotName']]
    candidate_name_split = raw_candidate_name.split()
    candidate_first_name = candidate_name_split[0]
    candidate_last_name = ' '.join(candidate_name_split[1:])

    raw_candidate_party = row[columns['PartyName']]
    party_regex = re.compile("Prefers (\w+) Party")
    party_result = party_regex.findall(raw_candidate_party)
    party_name = ''
    party_abbreviation = ''
    if party_result:
        party_name = party_result[0]
        party_abbreviation = party_name[0].upper()

    p = Party(party_name, party_abbreviation)

    c = Candidate(candidate_first_name, candidate_last_name)
    c.votes = row[columns['Votes']]

    r = Race(row[columns['RaceName']], row[columns['RaceJurisdictionTypeName']])
    r.total_votes = row[columns['TotalBallotsCastByRace']]

    print ''
    print c
    print c.first_name
    print c.last_name
    print ''

