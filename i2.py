import ollama

# Replace with your Ollama model and API key
model = "moondream"

def generate_response(prompt, history):
    '''
    This function is for generating response from the ollama.
    '''
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}] + history,
        stream=True
    )

    full_response = ""
    for chunk in response:
        full_response += chunk["message"]["content"]
    return full_response

def main():
    history = []
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            break
        history.append({"role": "user", "content": user_input})
        response = generate_response(user_input, history)
        print("Assistant:", response)

if __name__ == "__main__":
    main()