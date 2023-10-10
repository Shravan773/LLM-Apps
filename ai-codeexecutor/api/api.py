# api.py
import requests
import json

REPLIT_API_URL = "https://repl.it/api/v1/execute"
REPLIT_API_KEY = "YOUR_REPLIT_API_KEY"  # Replace this with your Repl.it API key

def execute_python_code(code: str) -> str:
    """
    Execute Python code using Repl.it's API.
    
    Args:
        code (str): Python code to be executed.
    
    Returns:
        str: Execution result from the API.
    """
    try:
        response = requests.post(REPLIT_API_URL, 
                                 data={"language": "python3", "code": code}, 
                                 headers={"Authorization": f"Bearer {REPLIT_API_KEY}"})
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        try:
            api_response = response.json()
            if 'output' in api_response:
                result = api_response['output']
                return result
            else:
                return "Error: Unable to get output from the API response."
        except json.JSONDecodeError:
            return "Error: Invalid JSON response from the API."

    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

# Example usage
if __name__ == "__main__":
    python_code = """
    def hello():
        return "Hello, World!"
    print(hello())
    """
    execution_result = execute_python_code(python_code)
    print("Execution Result:")
    print(execution_result)
