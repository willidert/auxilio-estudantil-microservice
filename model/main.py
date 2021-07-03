from flask import Flask, jsonify, request
import pickle

model = pickle.load(open('./model.sav', 'rb'))

app = Flask(__name__)

@app.route('/predicao/', methods=['POST'])
def predict():
	data = request.get_json()
	x = data['dados']
	res = model.predict(x)
	print(res)
	return jsonify(
		res=int(res[0])
	)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
