import torch
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import pandas as pd
import pickle

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
pickle.dump(tokenizer, open('tokenizer.pkl', 'wb'))
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
pickle.dump(device, open('device.pkl', 'wb'))
device = pickle.load(open('device.pkl', 'rb'))

t5_prepared_Text = "In addition to that, dump function is used to write the pickled representation of the object (the " \
                   "model in our example) to the open file. Dump format is as below and for further details you can " \
                   "refer to Python docs here. "
summaries = []

tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
summary_ids = model.generate(tokenized_text, num_beams=4, no_repeat_ngram_size=2, min_length=30, max_length=100, early_stopping=True)
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
summaries.append(output)
print("\n\nSummarized text: \n", output)


