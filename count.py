import sys
import pandas as pd
import csv

df = pd.read_csv('08_17.csv', header = None, delimiter="|",encoding='utf-8')

g=open('08_17_output.csv', 'wt')

states = [
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'NewHampshire',
    'NewJersey',
    'NewMexico',
    'NewYork',
    'NorthCarolina',
    'NorthDakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'RhodeIsland',
    'SouthCarolina',
    'SouthDakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'WestVirginia',
    'Wisconsin',
    'Wyoming']

abbr=['AK','AL','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN', 'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY', 'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 

for x in range(len(df.index)):
	try:	
		i = df.iloc[x,3].strip()
		a,b = i.split(",")
		b = b.strip()				
		print a + ' ' + b
		print ''
		if b == "Puerto Rico":
			print a
		elif b == 'USA' or b == 'US':
			for y in range(len(states)):
				if a.lower() == states[y].lower():
					count[y] += 1
		else:
			for z in range(len(abbr)):
				if b == abbr[z]:
					count[z] += 1
	except:
		print "exception occur."
	

	

writer = csv.writer(g)

for z in range(len(abbr)):	
	writer.writerow((abbr[z],count[z]))	

g.close()







