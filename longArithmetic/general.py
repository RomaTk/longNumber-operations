def isNumber(string):
	"""
This function checks is string represents int or float
	This function does not check type of arguments
isNumber(string)

arguments:
	"string":
		type:str
	"""
	def isPossibleFirstSymbol(string,symbol):
		numberOfSymbols=string.count(symbol);
		if numberOfSymbols>1:
			return False
		elif (numberOfSymbols==1)and(string[0]!=symbol):
			return False
		return True
	possibleSymbols="1234567890.+-";
	for symbol in string:
		if not(symbol in possibleSymbols):
			return False
	if not isPossibleFirstSymbol(string,"-"):
		return False
	if not isPossibleFirstSymbol(string,"+"):
		return False
	if string.count(".")>1:
		return False;
	return True

def sameLength(number1,number2):
	"""
This function aligns two numbers as int or float
	This function does not check are these strings represent integers or floats so you should check it before
	This function does not check type of arguments
sameLength(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	def beforeDot(number1,number2):
		b1=number1.index('.');
		b2=number2.index('.');
		if b1<b2:
			number1='0'*(b2-b1)+number1;
		elif b2<b1:
			number2='0'*(b1-b2)+number2;
		return number1,number2
	def afterDot(number1,number2):
		b1=len(number1)-1-number1.index('.');
		b2=len(number2)-1-number2.index('.');
		if b1<b2:
			number1=number1+'0'*(b2-b1);
		elif b2<b1:
			number2=number2+'0'*(b1-b2);
		return number1,number2
	if not("." in number1):
		number1+='.0';
	if not("." in number2):
		number2+='.0';
	number1,number2=beforeDot(number1,number2);
	number1,number2=afterDot(number1,number2);
	return number1,number2

def clearExtraZeros(string):
	"""
This function delete zeros in the beginning or end and present number as string int if possible
	This function does not check are these strings represent integers or floats so you should check it before
	This function does not check type of arguments
clearExtraZeros(string)

arguments:
	"string":
		type: str
	"""
	def beforeDot(string):
		i=0;
		while (string[i]=='0')and(i<len(string)-1):
			i+=1;
		string=string[i:];
		return string
	def afterDot(string):
		if "." in string:
			i=len(string)-1;
			while string[i]=='0':
				i-=1;
			string=string[:i+1];
		return string
	string=beforeDot(string);
	string=afterDot(string);
	if string[0]==".":
		string="0"+string;
	if string[-1]==".":
		string=string[:-1];
	return string

def getSymbolAndNumber(number):
	"""
This function return +/- and number without these numbers
	This function does not check are these strings represent integers or floats so you should check it before
	This function does not check type of arguments
getSymbolAndNumber(number)

arguments:
	"number":
		type: str
	"""
	if number[0]=="+":
		return "+",number[1:];
	elif number[0]=="-":
		return "-",number[1:];
	else:
		return "+",number;