from flask import Flask ,request,jsonify
import pickle

app = Flask(__name__)

class delivery_pickle:

    def predict(self,distance,weight):

        time = 0.5 + (distance*0.2) + (weight*0.1)
        return round(time, 2)


with open("delivery_model.pkl","rb") as file :
    mod = pickle.load(file)

@app.route("/")
def home():
    
    return "Delivery prediction API running"

@app.route("/predict",methods=["POST"])

def predict():
    data = request.get_json()

    distance = data["distance"]
    weight = data["weight"]

    output = mod.predict(distance,weight)

    return jsonify({
        "distance" : distance,
        "weight":weight,
        "estimated_delivery_time":output
    })

if __name__ == "__main__":
    app.run(debug=True)