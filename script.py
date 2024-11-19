
import os, sys, json
import pickle

### DATA INPUT

# run locally
if len(sys.argv) < 2:
	# hard code data path
	script_path = os.path.realpath(__file__).split("\\")
	data_path = "\\".join(script_path[:-1] + ["_temp", "script_inputs.d"])
# run from outside with args
else:
	# load data path from args
	data_path = sys.argv[-1]

# DESERIALIZE TEXT TO DATA
with open(data_path, 'rb') as f:
	data_in = pickle.load(f, encoding='latin1')
	data = json.loads(data_in)

	features = data["features"]
	num_clusters = int(data["num_clusters"])


### PROCESS

## run learning algorithm
## http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans
from sklearn import preprocessing

#mean 0, variance 1
scaler = preprocessing.StandardScaler().fit(features)
X = scaler.transform(features)

model = KMeans(n_clusters=num_clusters, init='k-means++')
model.fit(X)
y_pred = model.predict(X)

## output results
data_out = [y_pred.tolist(), scaler.inverse_transform(model.cluster_centers_).tolist()]
print(data_out)


### DATA OUTPUT
### SERIALIZE NEW DATA BACK TO TEXT
output_path = "\\".join(data_path.split("\\")[:-1] + ["script_output.d"])

with open(output_path, 'wb') as f:
	pickle.dump(data_out, f, protocol=2)

print("Done with output:")

# must be last print statement
print(output_path)