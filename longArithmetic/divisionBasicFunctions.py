from . import general
###############################################
#this type of division is only for int numbers#
###############################################
def divideStringsWithSign(number1="0",number2="1"):
	"""
This function divide two numbers as int inputed as strings
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
divideStringsWithSign(numer1="0",number2="1")

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	symbol1,number1=general.getSymbolAndNumber(number1);
	symbol2,number2=general.getSymbolAndNumber(number2);
	resultOfDivision=divideStrings(number1,number2);
	if (symbol1==symbol2)or(resultOfDivision[0]=="0"):
		return resultOfDivision[0],resultOfDivision[1]
	else:
		return "-"+resultOfDivision[0],resultOfDivision[1]
def divideStrings(number1,number2):
	"""
This function divide two numbers as int inputed as strings without +/- in the beginning
	This function does not check are these strings represent integers or floats so you should check it before
	And this function does not check type of arguments
compareStrings(number1,number2)

arguments:
	"number1":
		type: str
	"number2":
		type: str
	"""
	from .comparison import compareStrings
	from .substraction import minusStrings
	def basicOperationOfDivision(number1,number2):
		resultOfCompare=compareStrings(number1,number2);
		k=0;
		while not resultOfCompare=="<":
			number1=minusStrings(number1,number2);
			k+=1;
			resultOfCompare=compareStrings(number1,number2);
		if k==0:
			number1=general.clearExtraZeros(number1);
		return k,number1
	div="0"
	mod=number1
	toBegin=""
	start=0;
	isToContinue=True;
	while isToContinue:
		if len(number2)-len(toBegin)<=len(number1):
			partOfNumber1=toBegin+number1[start:start+len(number2)-len(toBegin)];
			resultOfCompare=compareStrings(partOfNumber1,number2);
			k=0;
			addIndex=start+len(number2)-len(toBegin);
			if resultOfCompare=="<":
				while addIndex+k<len(number1):
					partOfNumber1+=number1[addIndex+k];
					k+=1
					if not (compareStrings(partOfNumber1,number2)=="<"):
						break;
			#print("partOfNumber1:",partOfNumber1);
			div+="0"*(len(partOfNumber1)-len(toBegin)-1);
			if ((addIndex+k)>=len(number1))and(compareStrings(partOfNumber1,number2)=="<"):
				isToContinue=False;
			if len(partOfNumber1)!=len(toBegin):
				thisDiv,mod=basicOperationOfDivision(partOfNumber1,number2);
				div+=str(thisDiv);
				start+=len(partOfNumber1)-len(toBegin);
				if mod=="0":
					toBegin="";
				else:
					toBegin=mod;
		else:
			isToContinue=False;
	div=general.clearExtraZeros(div);
	return div,mod;

if __name__=="__main__":
	print(divideStrings(str(100),str(1)));