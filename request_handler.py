import openai
import models
# Set up OpenAI API
openai.api_key = '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'


def generate_recommendations(person, events):

    #prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format."

    prompt = ''''Сейчас я дам тебе информацию о пользователе и категориях, тебе нужно разработать рекомендации о мероприятиях на будущее, а так же статистику пользователя по категориям Be ITMO(be Healthy,be Fit,be Friendly,be Eco).
                В РЕЗУЛЬТАТЕ ВЫДАЙ ТОЛЬКО JSON в формате {'events':...,'stats':...}''
                Be ITMO - стиль жизни и корпоративная культура ИТМО, которая предлагает
    пользователю поддерживать активность и держать в фокусе шесть ключевых аспектов:
    персональное здоровье (be Healthy), активный образ жизни (be Fit), профессиональное
    развитие (be Pro), развитие социальных контактов и волонтерство (be Friendly), забота об
    окружающей среде (be Eco) и поддержание культуры открытости и коллаборации (be
    Open). \n'''
    # prompt += f"Имя: {person.name}\n"
    # prompt += f"Образование: {person.education}\n"
    # prompt += f"Работа: {person.job}\n"
    # prompt += f"Силы: {', '.join(person.powers)}\n"
    # prompt += f"Публикации: {', '.join(person.publications)}\n"
    # prompt += f"Проекты: {', '.join(person.projects)}\n"
    # prompt += f"Посещенные мероприятия: {', '.join(user_data['events'])}\n"
    # prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format."
    #prompt += person.__str__()
    #prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format."
    prompt = f"Person: {person}\nAvailable events: {events}\nGenerate event recommendations in a bullet list format. Leave event names unchanged.\nLeave only relevant events for specific person.\n"
    print(prompt)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=700,
        temperature=0.9,
        n=1,
        timeout=60  # Увеличение времени ожидания ответа до 60 секунд
    )
    recommended_events = response.choices[0].text

    # Send prompt to ChatGPT API for generating recommendations

    recommendations = [choice['text'].strip() for choice in response.choices]
    return recommendations
