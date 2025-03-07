from datasets import load_dataset

# Load your tarot_reading.json dataset
dataset = load_dataset('json', data_files={'train': 'data/tarot_reading.json'})

# Print dataset to verify it loaded correctly
print(dataset)
