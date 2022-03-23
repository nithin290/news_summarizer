import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
device = pickle.load(open('device.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    int_features = [str(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    content = final_features[0][0]

    preprocess_text = content.strip().replace("\n", "")
    # preprocess_text = "Original text: \n" + preprocess_text

    tokenized_text = tokenizer.encode(preprocess_text, return_tensors="pt").to(device)
    summary_ids = model.generate(tokenized_text, num_beams=4, no_repeat_ngram_size=2, min_length=30, max_length=100,
                                 early_stopping=True)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    output.strip()
    # output = "Summary: \n" + output
    return render_template('index.html', original_text=preprocess_text, summary=output)


@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    a = [np.array(list(data.values()))]

    content = a[0][0]

    preprocess_text = content.strip().replace("\n", "")
    preprocess_text += "summarize: " + preprocess_text
    # preprocess_text = "Original text: \n" + preprocess_text

    tokenized_text = tokenizer.encode(preprocess_text, return_tensors="pt").to(device)
    summary_ids = model.generate(tokenized_text, num_beams=4, no_repeat_ngram_size=2, min_length=30, max_length=100,
                                 early_stopping=True)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    # output = "Summary: \n" + output

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
