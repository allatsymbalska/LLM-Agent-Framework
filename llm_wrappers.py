# LLM wrappers module
# provides intent-classification wrappers for:
# - OpenAI GPT
# - Google Gemini
# - Anthropic Claude

# each wrapper:
# - accepts a user query (str)
# - returns exactly one intent label: FAQ or ORDER_STATUS

import os

# shared prompt builder

def _build_prompt(query: str) -> str:
    """
    Build a strict prompt for intent classification.
    The LLM must return ONLY one label: FAQ or ORDER_STATUS.
    """
    return f"""
You are an intent classifier.

Available agents:
- FAQ
- ORDER_STATUS

Rules:
- Respond with ONLY one agent label: FAQ or ORDER_STATUS
- Do NOT add punctuation, explanations, or extra text

User query: "{query}"
""".strip()


def _normalize_response(text: str) -> str:
    """
    Normalize and validate LLM output.
    Ensures only valid intent labels are returned.
    """
    label = text.strip().upper()

    if label not in {"FAQ", "ORDER_STATUS"}:
        raise RuntimeError(f"Invalid intent returned by LLM: '{text}'")

    return label



# OpenAI wrapper

def gpt_llm(query: str) -> str:
    """
    Intent classification using OpenAI GPT (Responses API).
    Requires OPENAI_API_KEY to be set in the environment.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("OpenAI SDK not installed. `pip install openai`")

    # check if API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")

    # create OpenAI client
    client = OpenAI(api_key=api_key)

    # build classification prompt
    prompt = _build_prompt(query)

    try:
        # send request to OpenAI Responses API
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            temperature=0
        )

        # normalize and return intent label
        return _normalize_response(response.output_text)

    except Exception as e:
        # surface errors
        raise RuntimeError(f"GPT wrapper error: {e}")



# Gemini wrapper

from google import genai

def gemini_llm(query: str) -> str:
    """
    Intent classification using Google Gemini.
    Requires GOOGLE_API_KEY to be set in the environment.
    """

    # check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")

    # create Gemini client
    client = genai.Client(api_key=api_key)

    # build classification prompt
    prompt = _build_prompt(query)

    try:
        # generate content using Gemini model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # extract and normalize model output
        text = response.text.strip().upper()

        # validate intent label
        if text not in ("FAQ", "ORDER_STATUS"):
            raise RuntimeError(f"Invalid intent returned by Gemini: '{text}'")

        return text

    except Exception as e:
        # surface errors
        raise RuntimeError(f"Gemini wrapper error: {e}")



# Claude wrapper

def claude_llm(query: str) -> str:
    """
    Intent classification using Anthropic Claude.
    Requires ANTHROPIC_API_KEY to be set in the environment.
    """
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("Anthropic SDK not installed. `pip install anthropic`")

    # check if API key is set
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set in environment")

    # create Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # build classification prompt
    prompt = _build_prompt(query)

    try:
        # send classification request to Claude
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=10,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # normalize and return intent label
        return _normalize_response(response.content[0].text)

    except Exception as e:
        # surface errors
        raise RuntimeError(f"Claude wrapper error: {e}")
