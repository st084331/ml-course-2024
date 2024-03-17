from sklearn.tree import DecisionTreeClassifier
import numpy as np


class AdaBoost:
    def __init__(self, n_learners=10):
        self.n_learners = n_learners
        self.learners = []
        self.learner_weights = []

    def fit(self, X, y):
        n_samples = X.shape[0]
        weights = np.full(n_samples, 1 / n_samples)

        for _ in range(self.n_learners):
            learner = DecisionTreeClassifier(max_depth=1)
            learner.fit(X, y, sample_weight=weights)
            predictions = learner.predict(X)

            error = np.sum(weights * (predictions != y))
            learner_weight = 0.5 * np.log((1 - error) / (error + 1e-10))

            weights *= np.exp(-learner_weight * y * predictions)
            weights /= np.sum(weights)

            self.learners.append(learner)
            self.learner_weights.append(learner_weight)

    def predict(self, X):
        learner_preds = np.array([learner.predict(X) for learner in self.learners])
        final_output = np.dot(self.learner_weights, learner_preds)
        return np.sign(final_output)