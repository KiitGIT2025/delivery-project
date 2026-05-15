import pickle

class delivery_pickle:

    def predict(self,distance,weight):

        time = 0.5 + (distance*0.2) + (weight*0.1)
        return round(time, 2)

mod = delivery_pickle()

with open("delivery_model.pkl","wb") as file:
    pickle.dump(mod,file)

print("Model saved !")