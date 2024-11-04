from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def test_setup():
    print("Testing OpenAI API connection...")
    
    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    print(f"API Key found: {'Yes' if api_key else 'No'}")
    
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        # Test API with a simple request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say hello!"}
            ]
        )
        
        print("\nAPI Test successful!")
        print(f"Response: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_setup()