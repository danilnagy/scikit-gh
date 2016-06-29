try:

	## import arguments
	import sys
	import pickle

	data = pickle.loads(str(sys.argv[1]))
	num_clusters = int(float(sys.argv[2]))

	## run learning algorithm
	## http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
	from sklearn.cluster import KMeans
	from sklearn import preprocessing

	#mean 0, variance 1
	scaler = preprocessing.StandardScaler().fit(data)
	X = scaler.transform(data)

	model = KMeans(n_clusters=num_clusters, init='k-means++')
	model.fit(X)
	y_pred = model.predict(X)

	## output results
	output = pickle.dumps([y_pred.tolist(), scaler.inverse_transform(model.cluster_centers_).tolist()])
	print output

except Exception as e:
	print e