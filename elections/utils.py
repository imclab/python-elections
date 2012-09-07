
def slugify(string):
    # Not yet implemented
    return string

def party_lookup(string):
    
    republican_list = ['Republican', 'G.O.P.', 'Gop']
    decocratic_list = ['Democrat', 'Democratic']
    
    if string in republican_list:
        return 'Republican'
    elif string in decocratic_list:
        return 'Democrat' 
    else:
        return string

def candidate_percentages(votes):
    return 100 * float(votes[0])/float(votes[1])    
    