from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num = X.shape[0]
    for i in range(num):
        class_scores = X[i].dot(W)
        class_scores -= np.max(class_scores)
        exp_scores = np.exp(class_scores) 
        probabilities = exp_scores / np.sum(exp_scores)

        loss += -np.log(probabilities [y[i]])    
        for j in range(W.shape[1]):
            if j == y[i]:
                dW[:, j] += (probabilities [j] - 1) * X[i]  
            else:
                dW[:, j] += probabilities [j] * X[i]  
   
    loss /= num
    dW /= num

    loss += reg * np.sum(W * W)
    dW += 2 * reg * W
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num = X.shape[0]
    class_scores = X.dot(W)
    class_scores -= np.max(class_scores, axis=1, keepdims=True)
    exp_scores = np.exp(class_scores)
    probabilities = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    correct_class_probabilities = probabilities[np.arange(num), y]
    loss = -np.sum(np.log(correct_class_probabilities)) / num
    loss += reg * np.sum(W * W)

    grad_scores = probabilities
    grad_scores[np.arange(num), y] -= 1
    dW = X.T.dot(grad_scores) / num
    dW += 2 * reg * W
    
    #pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
