from . import general
from . import summary

def multiplication(number1="0",number2="0"):
	"""
This function multiplies numbers as float or int inputed as strings
multiplication(number1="0",number2="0")

arguments:
	"number1":
		type: string
	"number2":
		type: string
	"""
	result="0";
	if (type(number1) is str)and(type(number2) is str):
		if (general.isNumber(number1))and(general.isNumber(number2)):
			result=multiplyStringsWithSymbol(number1,number2);
		else:
			raise Exception("Arguments should be like integers or floats in string");
	else:
		raise Exception("Type of arguments should be str");
	result=general.clearExtraZeros(result);
	return result
def multiplyStringsWithSymbol(number1="0",number2="0"):
	"""
This function multiply two numbers as int or float inputed as strings
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
multiplyStringsWithSymbol(number1="0",number2="0")

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	symbol1,number1=general.getSymbolAndNumber(number1);
	symbol2,number2=general.getSymbolAndNumber(number2);
	if (symbol1==symbol2)or(number1=="0")or(number2=="0"):
		return multiplyStrings(number1,number2);
	else:
		return "-"+multiplyStrings(number1,number2);
def multiplyStrings(number1="0",number2="0"):
	"""
This function multiply two numbers as int or float inputed as strings without +/- in the beginning
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
multiplyStrings(number1="0",number2="0")

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	def setPositionDot(numberStr=""):
		positionDot=len(numberStr);
		if "." in numberStr:
			positionDot=numberStr.index(".");
		return positionDot
	def deleteSymbolByPosition(st="",position=0):
		if (position>-1)and(position<len(st)):
			st=st[:position]+st[position+1:];
		return st
	def getNumberOfSymbolsAfterDot(dotPosition=0,lenOfString=""):
		return lenOfString-dotPosition;
	def addSymbol(st,position,symbol):
		return st[:position+1]+symbol+st[position+1:]
	number1=general.clearExtraZeros(number1);
	number2=general.clearExtraZeros(number2);
	result='0';
	positionDot1=setPositionDot(number1);
	positionDot2=setPositionDot(number2);
	number1=deleteSymbolByPosition(number1,positionDot1);
	number2=deleteSymbolByPosition(number2,positionDot2);
	for i in range(len(number2)-1,-1,-1):
		resultToSum=numeralWithNumber(number1,int(number2[i]))+'0'*(len(number2)-1-i);
		result=summary.sum(result,resultToSum);
	numbersAfterDot=getNumberOfSymbolsAfterDot(positionDot1,len(number1))+getNumberOfSymbolsAfterDot(positionDot2,len(number2));
	result=(numbersAfterDot-len(result))*"0"+result
	result=addSymbol(result,len(result)-1-numbersAfterDot,".");
	if result[0]==".":
		result="0"+result;
	if result[-1]==".":
		result=result+"0";
	result=general.clearExtraZeros(result);
	return result

def numeralWithNumber(number1="0",intNumber=0):
	"""
This function multiplies a number as int inputed as strings and int
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
numeralWithNumber(number1="0",intNumber=0)

arguments:
	"number1":
		type: string
	"intNumber":
		type: int
	"""
	addToNextLevel=0;
	result='';
	for i in range(len(number1)-1,-1,-1):
		calculatedMult=int(number1[i])*intNumber+addToNextLevel;
		result=str(calculatedMult%10)+result;
		addToNextLevel=calculatedMult//10;
	if addToNextLevel!=0:
		result=str(addToNextLevel)+result;
	return result;

if __name__=="__main__":
	print(multiplication("-154.6","-157.2"));
