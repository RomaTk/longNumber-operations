from . import general
def divide(number1="0",number2="0"):
	"""
This function divide two numbers as ints inputed as strings
	To return 2 ints(div and mod)
divide(number1="0",number2="0")

arguments:
	"number1":
		type:str
	"number2":
		type:str
	"""
	from . import divisionBasicFunctions
	if (type(number1) is str)and(type(number2) is str):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			if (not("." in number1))and(not("." in number2)):
				return divisionBasicFunctions.divideStringsWithSign(number1,number2);
			else:
				raise Exception("Arguments is not represented as ints");
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str and int");
def divideAsFloats(number1="0",number2="0",maxLenOfPartAfterDot=10):
	"""
This function divide two numbers as ints or floats inputed as strings
	To return float number as string with some amount of numbers after dot
divideToFloat(number1="0",number2="0",maxLenOfPartAfterDot=10)

arguments:
	"number1":
		type:str
	"number2":
		type:str
	"maxLenOfPartAfterDot":
		type:int
	"""
	result="";
	if (type(number1) is str)and(type(number2) is str)and(type(maxLenOfPartAfterDot) is int)and(maxLenOfPartAfterDot>-1):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			result=divideFloats(number1,number2,maxLenOfPartAfterDot);
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str and int");
	return result
def divideFloats(number1,number2,maxLenOfPartAfterDot):
	"""
This function divide two numbers as ints or floats inputed as strings
	To return float number as string with some amount of numbers after dot
	And this function does not check type of arguments
divideFloats(number1,number2,maxLenOfPartAfterDot)

arguments:
	"number1":
		type:str
	"number2":
		type:str
	"maxLenOfPartAfterDot":
		type:int
	"""
	def chooseSymbol(symbol1,symbol2):
		if symbol1==symbol2:
			return "+";
		else:
			return "-";
	def setPositionDot(numberStr=""):
		positionDot=len(numberStr);
		if "." in numberStr:
			positionDot=numberStr.index(".");
		return positionDot
	def deleteSymbolByPosition(st="",position=0):
		if (position>-1)and(position<len(st)):
			st=st[:position]+st[position+1:];
		return st
	def toInts(number1,number2):
		number1,number2=general.sameLength(number1,number2);
		positionDot1=setPositionDot(number1);
		positionDot2=setPositionDot(number2);
		number1=deleteSymbolByPosition(number1,positionDot1);
		number2=deleteSymbolByPosition(number2,positionDot2);
		return number1,number2
	from . import divisionBasicFunctions
	symbol1,number1=general.getSymbolAndNumber(number1);
	symbol2,number2=general.getSymbolAndNumber(number2);
	number1,number2=toInts(number1,number2);
	resultString=chooseSymbol(symbol1,symbol2);
	numbersAfterDot=0;
	beforeDot,afterDot=divisionBasicFunctions.divideStrings(number1,number2);
	resultString+=beforeDot;
	if maxLenOfPartAfterDot>0:
		resultString+='.';
		while numbersAfterDot<maxLenOfPartAfterDot:
			div,afterDot=divisionBasicFunctions.divideStrings(afterDot+'0',number2);
			resultString+=div
			numbersAfterDot+=1;
	resultSymbol,resultNumber=resultString[0],general.clearExtraZeros(resultString[1:]);
	if resultNumber=="0":
		result=resultNumber;
	elif resultSymbol=="+":
		result=resultNumber;
	else:
		result=resultSymbol+resultNumber;
	return result

if __name__=="__main__":
	print(divideAsFloats("3801.9010","434.5",7));
	print(divide("38019010","4345"));