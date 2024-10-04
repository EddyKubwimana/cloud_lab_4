from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

app = Flask(__name__)
api = Api(app)

# Download the VADER lexicon when the application starts up
nltk.download("vader_lexicon")

# class SentAnalysis(Resource):
#     def get(self):
#         sentence = request.args.get('q')

#         if not sentence:
#             return jsonify({'error': 'No sentence provided'}), 400

#         sid = SentimentIntensityAnalyzer()
#         score = sid.polarity_scores(sentence)["compound"]
#         if score > 0:
#             sentiment = "Positive"
#         else:
#             sentiment = "Negative"
        
#         #return jsonify({'sentiment': sentiment})

#         return json.dumps({"sentiment" :sentiment})

# api.add_resource(SentAnalysis, '/')

@app.route('/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        sentence = request.form['sentence']
        if not sentence:
            return jsonify({'error': 'No sentence provided'}), 400

        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(sentence)["compound"]
        if score > 0:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        return render_template('result.html', sentiment=sentiment)

    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
