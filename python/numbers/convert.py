
CATEGORY_DISTANCE = 0

UNITS = {
	"m": {
		"name": "Meter",
		"category": CATEGORY_DISTANCE
	},
	"au": {
		"name": "Astronomical unit",
		"category": CATEGORY_DISTANCE
	},
}

MULT_FACTORS = {
	"T": 1000000000000,
	"G": 1000000000,
	"M": 1000000,
	"k": 1000,
	"h": 100,
	"da": 10,
	"d": 0.1,
	"c": 0.01,
	"m": 0.001,
	"µ": 0.000001,
	"n": 0.000000001,
	"p": 0.000000000001
}

# conversions that are correct but cannot be applied with normal unit conversion eg N/kg -> m/(s^2)
CHEATING = []

def is_unit_supported(inp: str) -> bool:
	if inp in UNITS.keys():
		return True
	# i know, i should probably preprocess this list.
	for fact in MULT_FACTORS.keys():
		for unit in UNITS.keys():
			if fact + unit == inp:
				return True
	return False

def format_inp(inp: str) -> list:
	inp_list = inp.split()
	if len(inp_list)!=4 or inp_list[2]!='in' or not is_unit_supported(inp_list[1]) or not is_unit_supported(inp_list[3]):
		return []
	return [1]

def main() -> None:
	# input is awaited in the following format: 
	# x unit1 in unit2
	# where unit1 and unit2 can be any unit which is composed of units supported. (ex: N*m or m/s should work)
	# actually, it's even better than that, µin should work.
	inp = format_inp(input('Enter conversion (x unit1 in unit2): '))
	if len(inp)==0:
		print('Somtehing went wrong with your input. Please check the format and retry.')
		return
	print(inp)
	


if __name__=='__main__':
	main()