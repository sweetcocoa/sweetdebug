import sys
import os
from .dm import sweetdebug

def main():
    if len(sys.argv) < 2:
        print("Usage: sweetdebug <python_script.py> [script arguments...]")
        sys.exit(1)

    # Get the script path and its arguments
    script_path = sys.argv[1]
    script_args = sys.argv[2:]

    # Verify the script exists
    if not os.path.exists(script_path):
        print(f"Error: Script '{script_path}' not found")
        sys.exit(1)

    # Set up sweetdebug before running the script
    sweetdebug()

    # Prepare the script arguments
    sys.argv = [script_path] + script_args

    # Read and execute the script
    with open(script_path) as f:
        code = compile(f.read(), script_path, 'exec')
        # Create a new globals dictionary with __name__ set to __main__
        globals_dict = {
            '__name__': '__main__',
            '__file__': script_path,
            '__package__': None,
        }
        exec(code, globals_dict) 