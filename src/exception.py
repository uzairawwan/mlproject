## We will write our exception handling code over here 
'''
An exception, in the context of programming, refers to an unexpected event that occurs during the execution of
    a program that disrupts the normal flow of the program's instructions. 
When an exceptional condition arises, such as an error or unexpected behavior, 
    an exception object is typically created to represent this event.

Exceptions can occur for various reasons, including:

1. Errors in code logic: Such as attempting to perform an invalid operation, dividing by zero, 
    or accessing an index that is out of range.
2. External factors: Such as trying to access a file that doesn't exist or 
    encountering network issues while communicating with a server.
3. Resource limitations: Such as running out of memory or exceeding system-defined limits.

## In our case, we are going to write our own custom exception


The sys module in Python provides various functions and variables that are used to manipulate 
different parts of the Python runtime environment. 
It allows operating on the interpreter as it provides access to the variables and functions that 
interact strongly with the interpreter.

#Any exception that is getting controlled, the sys library will automatically have that information.
'''


import sys
import logging
# whenever I get an exception, I want to push this on my own custom message
def error_message_detail(error, error_detail:sys): # this means that error message is inside sys
# the variable below will give us information like on which file exception has occured
# and on which line number
    _,_,exc_tb = error_detail.exc_info() 
    # create an error message variable
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))

    return error_message    
    
#whenever an error raises, the above function will be called
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys): 
    # we are inheriting from exception 
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail) 
    # these are the paraeters that I have given in my custom exception 
    # whenever I raise this custom exception, it is inheriting the parent exception,
    # whatever error message that comes from this function, that particular error message willl come overhere.
    # The error detail has been tracked by sys

    def __str__(self):
        return self.error_message

    #
    #This will be common for the entire code, wherever the exception occurs
    #

'''
if __name__=="__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)   
      

import sys
import logging

# Configure logging to write to a file, setting the logging level to INFO
logging.basicConfig(filename='example.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def error_message_detail():
    # Get current exception information
    exc_type, exc_value, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{exc_value}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_detail=None): 
        # Initialize the base Exception class without a message
        super().__init__()
        # If error_detail is provided, use it to generate the error message
        if error_detail:
            self.error_message = error_message_detail()
        else:
            self.error_message = "A custom exception occurred."

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception:
        logging.exception("An exception occurred")
        raise CustomException()
'''


