# Age Telescope
#
# Brief: give the year you were born and a year 
# of interest to get the age you were,--or the
# amount of years you did not exist,--for every 
# year up to, or from, the year of interest.
#
# Author: Ron Rihoo
#

#import sys     # uncomment this line if you'll use argv[]

def main():
	print("Age Telescope")

	# take the two values at command line
	#year_1 = int(sys.argv[1])
	#year_2 = int(sys.argv[2])

	# preset them
	#year_1 = 1988
	#year_2 = 2015

	# take them from input
	year_1 = int(raw_input('Year of birth: '))
	year_2 = int(raw_input('Year to scope to: '))

	print ""       # for a newline in output

	calculateAge(year_1, year_2)


def calculateAge(born, scope):

	if (born < scope):
		print('Year\t\tAge')
		
		years = (scope - born)

		for i in range(years + 1):
			j = born + i
			print(str(j) + '\t\t' + str(i))

	elif (born > scope):
		print('Year\t\tYears before being born')

		years = (born - scope)

		for i in range(years + 1):
			j = scope + i
			print(str(j) + '\t\t' + str(years - i))
	elif (born == scope):
		print('0 years, mate.')
	else:
		print('Error: unexpected input, otherwise an unknown error has occured.')
  
main()
