# Structure of your solution to Assignment 1
import pandas as pd
import numpy as np


def analyze_tf_idf(arr, K):
    tf_ifd = None
    top_k = None

    # add your code here

    return tf_idf, top_k


if __name__ == "__main__":
    # Test Question 1
    arr = np.array([[0, 1, 0, 2, 0, 1], [1, 0, 1, 1, 2, 0], [0, 0, 2, 0, 0, 1]])

    print("\nQ1")
    tf_idf, top_k = analyze_tf_idf(arr, 3)
    print(top_k)