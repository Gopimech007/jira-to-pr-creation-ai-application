import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code_from_jira(title, description):
    prompt = f"""
    You are an expert Python developer.

    Task: Generate code based on this Jira ticket.
    Title: {title}
    Description: {description}

    Write clean, PEP8-compliant code with comments and error handling.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
