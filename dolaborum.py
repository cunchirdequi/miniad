def run_code(code, globals=None, locals=None):
    """
    Executes a given piece of code with optional global and local scope.
    
    Parameters:
    code (str): A string containing valid Python code.
    globals (dict, optional): Dictionary representing global scope.
    locals (dict, optional): Dictionary representing local scope.
    
    Returns:
    None
    """
    try:
        exec(code, globals, locals)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with controlled scope:
globals_dict = {}
locals_dict = {}

code_to_run = """
print('Hello, World!')
x = 5
y = 10
print('Sum:', x + y)
"""

run_code(code_to_run, globals_dict, locals_dict)
