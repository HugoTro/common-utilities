
CATEGORY_DISTANCE = 0

METRIC_UNITS = {
	"m": {
		"name": "meter",
		"category": CATEGORY_DISTANCE
	},
}

OTHER_UNITS = {
	# "l"
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

def is_unit_base(unit: str) -> bool:
	if unit in METRIC_UNITS.keys():
		return True
	return False

def find_metric_fact(unit: str) -> str | None:
	for fact in MULT_FACTORS.keys():
		if unit.find(fact) == 0:
			return fact
	return None

def is_unit_metric(unit: str) -> bool:
	for m_unit in METRIC_UNITS.keys():
		if m_unit == unit:
				return True
		m_fact = find_metric_fact(unit)
		if m_fact is not None and len(m_fact)+len(m_unit)==len(unit):
			return True

def is_unit_supported(inp: str) -> bool:
	if is_unit_metric(inp) or inp in OTHER_UNITS.keys():
		return True
	return False

def find_coef(inp: list) -> float:
	# we know list is in this format
	# [value, unit_from, unit_to]
	coef = 1
	if is_unit_metric(inp[1]) and is_unit_metric(inp[2]):
		# that's easy, we just need to get the coefficient from each to the base unit.
		if not is_unit_base(inp[1]):
			m_fact = find_metric_fact(inp[1])
			coef *= MULT_FACTORS[m_fact]
		# else the factor is just 1
		if not is_unit_base(inp[2]):
			m_fact = find_metric_fact(inp[2])
			coef /= MULT_FACTORS[m_fact]
	else:
		coef = 0
	return coef

# CAREFUL: Use input formatting before calling this function.
def convert(value: float | list, unit_in: str = None, unit_out: str = None) -> float:
	if type(value) == list:
		cf = find_coef(value)
		return value[0]*cf
	cf = find_coef([value, unit_in, unit_out])
	return value*cf

def format_inp(inp: str) -> list:
	inp_list = inp.split()
	if len(inp_list)!=4 or inp_list[2]!='in' or not is_unit_supported(inp_list[1]) or not is_unit_supported(inp_list[3]):
		return []
	try:
		inp_list[0] = float(inp_list[0])
	except:
		return []
	del inp_list[2]
	return inp_list

def main() -> None:
	# input is awaited in the following format: 
	# x unit1 in unit2
	# where unit1 and unit2 can be any unit which is supported, NOT YET - which is composed of units supported. (ex: N*m or m/s should work)
	# actually, it's even better than that, µin should work.
	inp = format_inp(input('Enter conversion (x unit1 in unit2): '))
	if len(inp)==0:
		print('Something went wrong with your input. Please check the format and retry.')
		return
	res = convert(inp)
	print(res, inp[2])


if __name__=='__main__':
	main()