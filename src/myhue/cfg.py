"""
Global settings

Click's ctx.obj could mostly be used for these, but is not available to the
exception handler in __init__.py
"""

traceback = None # Print tracebacks for qhue exceptions
bridge = None # The qhue bridge we are working with
pprint = None # Function for pretty printing Python objects
indent = None # Indent for pretty printers
