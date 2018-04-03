NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
#TODO: I could have used a dict to dedupe    
    dedup = []
    for name in NAMES:
        if name not in dedup:
            dedup.append(name)
    return [name.title()  for name in dedup]        



def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    #TODO: Refactor this code, this is horrible
    names2 = []
    for name in names:
        first, last = name.split()
        names2.append(', '.join((last, first)))

    names2.sort(reverse = True)

    names3 = []

    for name in names2:
    	last, first = name.split(', ')
    	names3.append(' '.join((first.strip().title(), last.strip().title())))

    print(names3)
    return names3



def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    #TODO: refactor this code to use min with key
    names = dedup_and_title_case_names(names)
    shortest = ''
    for name in names:
    	first,last = name.split()
    	if shortest == '':
    		shortest = first
    	else:
    		if len(first) < len(shortest):
    			shortest = first
    print(shortest.title())
    return shortest.title()


def main():
	shortest_first_name(NAMES)


if __name__ == '__main__':
	main()