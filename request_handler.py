import openai

# Set up OpenAI API
openai.api_key = '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'
#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

def generate_recommendations(person, events):
    prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format."

    # Send prompt to ChatGPT API for generating recommendations
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=3,  # Adjust the number of recommendations you want
        temperature=0.7,
        stop=None,
    )

    recommendations = [choice['text'].strip() for choice in response.choices]
    return recommendations


# Example usage
person_info = "John Doe"
available_events = ["Event A", "Event B", "Event C", "Event D"]


