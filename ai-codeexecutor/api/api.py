# api.py
import requests
import json

API_BASE_URL = "https://tgapi-7d0b0583d985.herokuapp.com/api/v1/coderunner/execute"  # Replace this with the actual API endpoint URL

def execute_gpt_code(code: str) -> str:
    """
    Execute Python code using the GPT model via the API endpoint.
    
    Args:
        code (str): Python code to be executed.
    
    Returns:
        str: Execution result from the API.
    """a
    try:
        response = requests.post(API_BASE_URL, json={"code": code})
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        try:
            api_response = response.json()
            if 'result' in api_response:
                result = api_response['result']
                return result
            else:
                return "Error: 'result' key not found in the API response."
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
    execution_result = execute_gpt_code(python_code)
    print("Execution Result:")
    print(execution_result)
