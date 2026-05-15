import pickle
from model import delivery_pickle

mod = delivery_pickle()

with open("delivery_model.pkl", "wb") as file:
    pickle.dump(mod, file)

print("Model saved!")
