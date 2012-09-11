
def slugify(string):
    # Not yet implemented
    return string

def party_lookup(string):
    
    republican_list = ['Republican', 'G.O.P.', 'Gop', 'Hope&change']
    decocratic_list = ['Democrat', 'Democratic', 'Independent Dem.']

    if string in republican_list:
        return 'Republican'
    elif string in decocratic_list:
        return 'Democrat' 
    else:
        return string

def candidate_percentages(votes):
    return 100 * float(votes[0])/float(votes[1])    
    
    
 # (Prefers    Republican  Party) = R
#  (Prefers (R) Hope&change  Party) = R
#  (Prefers Democrat  Party) = D
#  (Prefers Democratic  Party) = D
#  (Prefers Democratic  Party) = D
#  (Prefers G.O.P. Party) = R
#  (Prefers Gop Party) = R
#  (Prefers Green Party) = G
#  (Prefers Independent Dem.  Party) = D 
#  (Prefers Independent  Party) = I 
#  (Prefers Independent-Gop  Party) = I-R 
#  (Prefers Non-partisan  Party)  = I
#  (Prefers Republican  Party) = R
#  (Prefers Republican  Party) = R
#  (Prefers Socialist Altern  Party) = SA
#  (States No Party  Preference) = NPP
#  Constitution Party  Nominees = C
#  Democratic Party  Nominees = D
#  Green Party Nominees = G
#  Justice Party Nominees = J
#  Libertarian Party  Nominees = L
#  Republican Party  Nominees = R
#  Socialism & Liberation Party  Nominees = S&L
#  Socialist Workers Party  Nominees = SW

#  C-Constitution; D-Democrat;
#  G-Green; I-Independent; R-Republican;
#  L-Libertarian; P-Progressive;
#  S&L-Socialism & Liberation; SW-Socialist
#  Workers;
#  J-Justice; SA-Socialist Altern. Party;
#  There is also one labeled Independent-GOP and I have listed it as I-R and I made No Party Preference – NPP.