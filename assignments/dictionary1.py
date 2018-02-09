#DICTIONARY
'''
The keys should include name, age, country of birth, favorite language.
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"

  hash = {}
  hash['word'] = 'garfield'
  hash['count'] = 42
  s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
  # 'I want 42 copies of garfield'
'''
names = {}
names = {
    'name' : 'Suzanne',
    'age' : 40,
    'birth_country' : 'United States',
    'program_lang' : 'Python',
    }
#for key,data in Names.iteritems():
#    print key, '=', data
#print names   

def my_info(names):
    print 'My name is', names['name']
    print 'My age is', names['age']
    print 'My country of birth is', names['birth_country']
    print 'My favorite language is', names['program_lang']
my_info(names)

