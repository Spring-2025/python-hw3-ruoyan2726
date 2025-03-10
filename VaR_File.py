# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eAsDTfw4J5xg2P9uif2Xo74HiMyyt9Kv
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r, confidence, principal=1):
    alpha = 1 - confidence
    var_percentile = np.percentile(r, alpha * 100)

    out = principal * abs(var_percentile)

    plt.hist(r, bins=50, alpha=0.75, color='blue', edgecolor='black')
    plt.axvline(var_percentile, color='red', linestyle='dashed', linewidth=2, label=f'VaR ({confidence*100}%)')
    plt.legend()
    plt.show()

    return out

def percent_var(r, confidence):
    alpha = 1 - confidence
    out = np.percentile(r, alpha * 100)

    plt.hist(r, bins=50, alpha=0.75, color='blue', edgecolor='black')
    plt.axvline(out, color='red', linestyle='dashed', linewidth=2, label=f'Percentile ({confidence*100}%)')
    plt.legend()
    plt.show()

    return abs(out)


# Example tools: percentile
returns = np.random.normal(0, 1, 10000)
print(np.percentile(returns, 97.72))

# Unit test
r = np.random.normal(0.05, 0.03, 1000000)
probability2SD = norm.cdf(2)  # Probability under normal curve within 2 standard deviations

my_confidence = probability2SD
my_percent_var = percent_var(r, my_confidence )
print(np.round(my_percent_var, 2) == 0.01)