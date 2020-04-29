from sklearn import tree
features = [[140, 1], [130, 1], [160, 0], [170, 0]]
labels = ["s1", "s1", "s2", "s2"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print("je suis capable de prédire la solution à " + str(clf.score(features, labels) * 100) + "%")
print("la solution que je propose est : " + clf.predict([[150, 0]])[0])
