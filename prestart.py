from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
import ruprompts

"""
Don't look at this file
It just for download pretrained models before start server
"""

tokenizer = AutoTokenizer.from_pretrained(
            "sberbank-ai/rugpt2large")
model = AutoModelWithLMHead.from_pretrained(
            "sberbank-ai/rugpt2large")
ppln = pipeline('text2text-generation-with-prompt',
                        prompt='konodyuk/prompt_rugpt3large_title_mlsum')