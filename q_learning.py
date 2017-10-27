import gym, os, sys
import numpy as np
import matplotlib.pyplot as plt
from gym import wrappers
from datetime import datetime
from sklearn.pipline import FeatureUnion
from sklearn.kernel_approximation import RBFSampler
from q_learning_bins import plot_running_avg

class SGDRegressor:
    def __init__(self, D):
        self.w = np.random.randn(D) / np.sqrt(D)
        self.lr = 0.1

    def partial_fit(self, X, Y):
        self.w += self.lr * (Y - X.dot(self.w)).dot(X)

    def predict(self, X):
        return X.dot(self.w)
    