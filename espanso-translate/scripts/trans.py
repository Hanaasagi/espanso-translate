import os
import sys
import openai

openai.api_key = os.environ.get("ESPANSO_OPENAI_KEY")

system_prompt = """\
I want you to act as an {lang} translator, spelling corrector and improver.\
I will speak to you in English language , \
translate it and answer in the corrected and improved version of my text, in {lang}. \
I want you to replace my simplified entry-level words and sentences with more beautiful and elegant, \
upper level {lang} words and sentences. Keep the meaning same, but make them more literary. \
I want you to only reply the correction, the improvements and nothing else, do not write explanations.\
"""


def translate(model: str, dest_lang: str, content: str) -> str:
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt.format(lang=dest_lang)},
            {
                "role": "user",
                "content": content,
            },
        ],
    )

    result = ""
    for choice in response.choices:
        result += choice.message.content

    return result


if __name__ == "__main__":
    dest_lang = sys.argv[1]
    model = os.environ.get("ESPANSO_AI_MODEL", "gpt-3.5-turbo")
    content = sys.argv[2]
    result = translate(model=model, dest_lang=dest_lang, content=content)
    print(result)
