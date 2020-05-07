# ***************************************************************************************
# *    Title: Python Decorators for Error handling
# *    Author: Vighnesh SK
# *    Date: Oct 15, 2018
# *    Availability: https://dev.to/booterror/python-decorators-for-error-handling-50eb
# *
# ***************************************************************************************

import sys
import traceback


def safe_run(func):
    def func_wrapper(*args, **kwargs):

        try:
            func(*args, **kwargs)

        except Exception as e:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)

            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" % ex_value)
            print("Exception file info : %s" % trace_back)
            return None

    return func_wrapper