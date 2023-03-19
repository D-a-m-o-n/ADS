import openai

openai.api_key = "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"

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()



