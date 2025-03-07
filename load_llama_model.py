from transformers import LlamaTokenizer, LlamaForCausalLM

# Load the tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained("huggingface/llama-7b")
model = LlamaForCausalLM.from_pretrained("huggingface/llama-7b")

print("Model and tokenizer loaded successfully!")
