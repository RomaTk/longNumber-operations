##################################################################
#                                                                #
#  Each of this functions get 2 strings which represent strings  ###########################################################################################################
#  And return result or it will be raised an error               #                                                                                                         #
#  All inputed data is checked so it should not be any problems  # Special: numbers should be as integer or float without any exponent it can have + or - in the beginning.#
##################################################################          Not more than one dot. Other symbols is numerals                                               #
                                                                 #                                                                                                         #
                                                                 ###########################################################################################################

"""
	Compare function return strings:
	<, = or > depending in values
"""
from .comparison import compare

"""
	Sum return result of summary of two numbers
"""
from .summary import sum

"""
	Minus return result of substraction of two numbers
"""
from .substraction import minus

"""
	multiply return result of multiplication of two numbers
"""
from .multiplication import multiplication as multiply

"""
	divide return the integer part and modulo of the result of division of two ints
"""
from .division import divide

"""
	divide return float with some signs after dot of division of two numbers
	The third parametr of maximum possible numbers after dot is the third
"""
from .division import divideAsFloats
