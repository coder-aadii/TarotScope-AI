from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
import torch

# Load your dataset
dataset = load_dataset('json', data_files='data/tarot_reading.json')

# Load GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Add a padding token to the tokenizer (GPT-2 doesn't have one by default)
tokenizer.pad_token = tokenizer.eos_token  # Use the EOS token as padding

# Tokenize the dataset and make sure labels are provided for training
def tokenize_function(examples):
    tokenized = tokenizer(examples['interpretation'], padding='max_length', truncation=True)
    tokenized['labels'] = tokenized['input_ids'].copy()  # Use input_ids as labels
    return tokenized

# Apply tokenization
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Split the dataset into train and eval
tokenized_dataset = tokenized_dataset['train'].train_test_split(test_size=0.2)

# Load GPT-2 model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',  # Directory to save the model
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,  # Adjust batch size based on your system's memory
    per_device_eval_batch_size=4,
    num_train_epochs=3,  # You can increase this for better training
    save_steps=10_000,
    save_total_limit=2,  # Limit the total number of checkpoints to save space
    logging_dir='./logs',  # Log directory for TensorBoard
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],  # Use the train dataset
    eval_dataset=tokenized_dataset['test'],  # Use the eval dataset
)

# Start training
trainer.train()

# Save the fine-tuned model and tokenizer
model.save_pretrained('./fine_tuned_gpt2')
tokenizer.save_pretrained('./fine_tuned_gpt2')
