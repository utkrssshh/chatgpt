import openai
api_key = 'API-KEY'
openai.api_key = api_key
def chat_with_gpt(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",  # GPT-3.5 engine
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text
while True:
    user_input = input("You : ")
    if user_input.upper()=="QUIT":
        print("Goodbye!!!")
        break
    response = chat_with_gpt(user_input)
    print(f"AI : {response}")