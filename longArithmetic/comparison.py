from . import general
def compare(number1="0",number2="0"):
	"""
This function compare two numbers as ints or floats inputed as strings
compare(number1="0",number2="0")

arguments:
	"number1":
		type:str
	"number2":
		type:str
	"""
	result="";
	if (type(number1) is str)and(type(number2) is str):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			result=compareStringsWithSign(number1,number2);
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str");
	return result
def compareStringsWithSign(number1,number2):
	"""
This function compare two numbers as int or float inputed as strings
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
compareStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	symbol1,numberCopy1=general.getSymbolAndNumber(number1);
	symbol2,numberCopy2=general.getSymbolAndNumber(number2);
	if (numberCopy1.count("0")+numberCopy1.count("."))==len(numberCopy1):
		numberCopy1="0";
		symbol1="+";
	if (numberCopy2.count("0")+numberCopy2.count("."))==len(numberCopy2):
		numberCopy2="0";
		symbol2="+";
	if symbol1==symbol2:
		result=compareStrings(numberCopy1,numberCopy2);
	elif symbol1=="-":
		result="<"
	else:
		result=">"
	return result
def compareStrings(number1,number2):
	"""
This function compare two numbers as int or float inputed as strings without +/- in the beginning
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
compareStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	def biggerOrSmaller(number1,number2):
		for i in range(len(number1)):
			n1=int(number1[i]);
			n2=int(number2[i]);
			if n1<n2:
				return "<";
			elif n1>n2:
				return ">"
	number1,number2=general.sameLength(number1,number2);
	number1=number1.replace(".",'');
	number2=number2.replace(".",'');
	if number1==number2:
		return "="
	else:
		return biggerOrSmaller(number1,number2);

if __name__=="__main__":
	print(compare("3","12"));