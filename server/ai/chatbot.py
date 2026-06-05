import os

from openai import OpenAI

from ai.recommendation_engine import build_recommendations, build_trip_plan


SYSTEM_PROMPT = (
    "You are All Tourism Assistant, a practical tourism assistant for an aggregator platform. "
    "Recommend destinations, hotels, resorts, restaurants, routes, safety guidance, and official booking paths. "
    "When the user gives a budget, recommend matching budget-first hotels, resorts, attractions, day-wise plans, and booking options. "
    "Never claim All Tourism Assistant processes payments; tell users bookings happen on official provider websites."
)


def tourism_chat_reply(message):
    api_key = os.getenv("GROK_API_KEY")
    model = os.getenv("GROK_MODEL", "grok-3-mini")
    base_url = os.getenv("GROK_BASE_URL", "https://api.x.ai/v1")
    if api_key and not api_key.startswith("replace-with"):
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            temperature=0.45,
            max_tokens=700
        )
        return response.choices[0].message.content

    budget = _extract_budget(message)
    recs = build_recommendations(budget=budget, interests=message)
    plan = build_trip_plan(recs["destination"], budget, 3, message)
    return (
        f"I can help. For a Rs. {budget} budget, I recommend {recs['destination']}. "
        f"Budget-first stays: {', '.join(recs['hotels'][:2])}. "
        f"Resort options: {', '.join(recs['resorts'][:2])}. "
        f"Attractions: {', '.join(recs['places'][:3])}. "
        f"Day 1 plan: {plan['schedule'][0]['theme']} with {plan['schedule'][0]['items'][0]['activity']}. "
        "Use OpenStreetMap navigation for live routes, keep 112 and 108 saved, avoid isolated late-night routes, "
        "and complete bookings only on the official external provider website using the Book Now links."
    )


def _extract_budget(message):
    text = str(message).replace(",", "")
    numbers = []
    current = ""
    for char in text:
        if char.isdigit():
            current += char
        elif current:
            numbers.append(int(current))
            current = ""
    if current:
        numbers.append(int(current))
    return max(numbers) if numbers else 15000
