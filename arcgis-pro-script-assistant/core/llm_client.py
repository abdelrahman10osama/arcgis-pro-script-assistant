from groq import Groq
from prompts.system_prompt import SYSTEM_PROMPT

def ask_groq(user_prompt, api_key, model_name, temperature):

    client = Groq(api_key=api_key)

    final_prompt = f"""
    {SYSTEM_PROMPT}

    USER QUESTION:
    {user_prompt}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": final_prompt,
            }
        ],
        model=model_name,
        temperature=temperature,
    )

    return chat_completion.choices[0].message.content