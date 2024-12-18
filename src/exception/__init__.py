import os , sys

class CustomException(Exception):
    def __init__(self , error_message:Exception ,error_details:sys):
        self.error_message = CustomException.get_error_location_and_details(
            error_message = error_message,
            error_details = error_details
        )

    @staticmethod
    def get_error_location_and_details(error_message:Exception , error_details:sys):

        _,_,exc_tb = error_details.exc_info()

        exception_block_line_no = exc_tb.tb_frame.f_lineno
        try_block_line_no = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename

        detailed_message = f"""Error Occured during execution of file: {file_name}
          at try block line no: {try_block_line_no} and 
          exception block line no: {exception_block_line_no}"""


        return detailed_message


    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()

