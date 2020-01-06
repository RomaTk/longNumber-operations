from . import general


def sum(number1="0",number2="0"):
	"""
This function summarizes two numbers as int or float inputed as strings
sum(number1="",number2="")

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	if (type(number1) is str)and(type(number2) is str):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			result=sumStringsWithSign(number1,number2);
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str");
	return result

def sumStringsWithSign(number1,number2):
	"""
This function summarizes two numbers as int or float inputed as strings
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
sumStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	from .comparison import compareStrings
	from .substraction import minusStrings
	symbol1,numberCopy1=general.getSymbolAndNumber(number1);
	symbol2,numberCopy2=general.getSymbolAndNumber(number2);
	if symbol1==symbol2:
		result=symbol1+sumStrings(numberCopy1,numberCopy2);
	elif compareStrings(numberCopy1,numberCopy2)==">":
		result=symbol1+minusStrings(numberCopy1,numberCopy2);
	else:
		result=symbol2+minusStrings(numberCopy2,numberCopy1);
	#number to normal view
	resultSymbol,resultNumber=result[0],result[1:];
	if resultNumber=="0":
		result=resultNumber;
	elif resultSymbol=="+":
		result=resultNumber;
	else:
		result=resultSymbol+resultNumber;
	return result

def sumStrings(number1,number2):
	"""
This function summarizes two numbers as int or float inputed as strings without +/- in the beginning
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
sumStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	number1,number2=general.sameLength(number1,number2);
	addToNextLevel=0;
	result='';
	for i in range(len(number1)-1,-1,-1):
		if (number1[i]!='.'):
			calculatedSum=int(number1[i])+int(number2[i])+addToNextLevel;
			result=str(calculatedSum%10)+result;
			addToNextLevel=calculatedSum//10;
		else:
			result='.'+result;
	if addToNextLevel!=0:
		result=str(addToNextLevel)+result;
	result=general.clearExtraZeros(result);
	return result

if __name__=="__main__":
	print(sum("10.3","140"));
