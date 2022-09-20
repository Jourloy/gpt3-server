##########################################################
# This file is only for prepared models for your system. #
# It download models before backend start                #
##########################################################

from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline

tokenizer = AutoTokenizer.from_pretrained(
            "sberbank-ai/rugpt2large")
model = AutoModelWithLMHead.from_pretrained(
            "sberbank-ai/rugpt2large")
ppln = pipeline('text2text-generation-with-prompt',
                        prompt='konodyuk/prompt_rugpt3large_title_mlsum')