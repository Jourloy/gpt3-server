from transformers import AutoTokenizer, AutoModelWithLMHead


class RuGPT3:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(
            "sberbank-ai/rugpt2large")
        self.model = AutoModelWithLMHead.from_pretrained(
            "sberbank-ai/rugpt2large")
        self.model.to("cpu")

    def generate(self, text, maxLength) -> str:
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        input_ids = input_ids.to("cpu")
        print(maxLength+len(text))
        greedy_output = self.model.generate(
            input_ids,
            max_length=maxLength+len(text),
            top_k=0,
            top_p=0.96,
            temperature=0.9,
            repetition_penalty=1.0,
            do_sample=True,
            num_return_sequences=1
        )
        return self.tokenizer.decode(greedy_output[0], clean_up_tokenization_spaces=True)
