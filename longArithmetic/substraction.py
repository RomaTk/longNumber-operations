from . import general

def minus(number1="0",number2="0"):
	"""
This function subtracts two numbers as int or float inputed as strings
minus(number1="",number2="")

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	if (type(number1) is str)and(type(number2) is str):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			result=minusStringsWithSign(number1,number2);
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str");
	return result

def minusStringsWithSign(number1,number2):
	"""
This function subtracts two numbers as int or float inputed as strings
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
minusStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	from .comparison import compareStrings
	from .summary import sumStrings
	symbol1,numberCopy1=general.getSymbolAndNumber(number1);
	symbol2,numberCopy2=general.getSymbolAndNumber(number2);
	if symbol1==symbol2:
		compareSimbol=compareStrings(numberCopy1,numberCopy2);
		if (compareSimbol==">")or(compareSimbol=="="):
			result=symbol1+minusStrings(numberCopy1,numberCopy2);
		else:
			if symbol2=="+":
				result="-"+minusStrings(numberCopy2,numberCopy1);
			else:
				result="+"+minusStrings(numberCopy2,numberCopy1);
	else:
		result=symbol1+sumStrings(numberCopy1,numberCopy2);
	resultSymbol,resultNumber=result[0],result[1:];
	if resultNumber=="0":
		result=resultNumber;
	elif resultSymbol=="+":
		result=resultNumber;
	else:
		result=resultSymbol+resultNumber;
	return result

def minusStrings(number1,number2):
	"""
This function subtracts two numbers as int or float inputed as strings without +/- in the beginning
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
minusStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	number1,number2=general.sameLength(number1,number2);
	minusFromNextLevel=0;
	result='';
	for i in range(len(number1)-1,-1,-1):
		if (number1[i]!='.'):
			n1=int(number1[i])-minusFromNextLevel;
			n2=int(number2[i]);
			if n1>=n2:
				result=str(n1-n2)+result;
				minusFromNextLevel=0;
			else:
				result=str(n1+10-n2)+result;
				minusFromNextLevel=1;
		else:
			result='.'+result;
	result=general.clearExtraZeros(result)
	return result

if __name__=="__main__":
	print(minus(number1="0.0321",number2="0.0321"));