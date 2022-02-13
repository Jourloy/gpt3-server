from rudalle import get_tokenizer, get_vae

from rudolph.model import get_rudolph_model
from rudolph.pipelines import generate_codebooks, self_reranking_by_text

import torch


class RuDolph:
    def __init__(self) -> None:
        self.device = 'cpu'
        self.model = get_rudolph_model(
            '350M', device=self.device).to(self.device)
        self.tokenizer = get_tokenizer()
        self.vae = get_vae(dwt=False).to(self.device)

        self.bs, self.top_k, self.top_p = 48, 512, 0.9

    def generate(self, text):
        images = []
        with torch.no_grad():
            codebooks = generate_codebooks(
                text, self.tokenizer, self.model, top_k=self.top_k, images_num=1, top_p=self.top_p, bs=self.bs)
            ppl_text = self_reranking_by_text(
                text, codebooks, self.tokenizer, self.model, bs=self.bs)
            images = self.vae.decode(codebooks[ppl_text.argsort()[:9]])
        return images[0]
