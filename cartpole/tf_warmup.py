import tensorflow as tf
from . import q_learning


class SGDRegressor:
  def __init__(self, D):
    print("Hello TensorFlow!")
    lr = 0.1

    self.w = tf.Variable(tf.random_normal(shape=(D, 1)), name='w')
    self.X = tf.placeholder(tf.float32, shape=(None, D), name='X')
    self.Y = tf.placeholder(tf.float32, shape=(None,), name='Y')

    Y_hat = tf.reshape( tf.matmul(self.X, self.w), [-1] )
    delta = self.Y - Y_hat
    cost = tf.reduce_sum(delta * delta)

    self.train_op = tf.train.GradientDescentOptimizer(lr).minimize(cost)
    self.predict_op = Y_hat

    init = tf.global_variables_initializer()
    self.session = tf.InteractiveSession()
    self.session.run(init)

  def partial_fit(self, X, Y):
    self.session.run(self.train_op, feed_dict={self.X: X, self.Y: Y})

  def predict(self, X):
    return self.session.run(self.predict_op, feed_dict={self.X: X})


if __name__ == '__main__':
  q_learning.SGDRegressor = SGDRegressor
  q_learning.main()
