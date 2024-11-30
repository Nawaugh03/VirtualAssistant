from transformers import AutoTokenizer, AutoModelForCausalLM
import os
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
