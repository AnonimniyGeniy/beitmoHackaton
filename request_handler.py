import openai
import models
# Set up OpenAI API
openai.api_key = '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'


def generate_recommendations(person, events):

    prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format. " \
             f"Leave event names unchanged.\nLeave 4 most relevant events for specific person.\n"
    print(prompt)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.9,
        n=1,
        timeout=60  # Увеличение времени ожидания ответа до 60 секунд
    )
    recommended_events = response.choices[0].text

    # Send prompt to ChatGPT API for generating recommendations

    recommendations = [choice['text'].strip() for choice in response.choices]
    return recommendations
