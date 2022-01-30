from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location':util.get_location_names()
     })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predict_home_rent', methods=['POST'])
def predict_home_rent():
    newadd = request.form['newadd']
    bedroom = int(request.form['bedroom'])
    bathrooms = int(request.form['bathrooms'])
    area = float(request.form['area'])
    response = jsonify({
        'estimated_rent': util.get_estimated_rent(newadd, bedroom, bathrooms, area)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()
