from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Load OpenAI API key
openai.api_key = "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"


@app.route('/completion')
def completion():
    prompt = request.args.get('prompt')
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    return jsonify({'response': response.choices[0].text.strip()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)