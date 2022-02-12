import ruprompts
from transformers import pipeline


class RuTitle():
    def __init__(self) -> None:
        pass

    def generate(self, text):
        ppln = pipeline('text2text-generation-with-prompt',
                        prompt='konodyuk/prompt_rugpt3large_title_mlsum')

        generated = ppln(text)
        return generated[0]['generated_text']
