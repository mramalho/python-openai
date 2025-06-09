import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_chatgpt_response():
    # Fixed prompt that will be sent to ChatGPT
    prompt = "What are the three laws of robotics?"
    
    try:
        # Make the API call to ChatGPT
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response
        return response.choices[0].message.content
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY environment variable is not set")
        exit(1)
    
    # Get and print the response
    response = get_chatgpt_response()
    print("\nChatGPT Response:")
    print("-" * 50)
    print(response)
    print("-" * 50) 