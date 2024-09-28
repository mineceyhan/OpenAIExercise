# Calculating Cosine Similarity

import numpy as np 

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

# (1 * 4) + (2 * 5) + (3 * 6)
dot_product = np.dot(v1, v2)
print(dot_product)

# square root of (1^2 + 2^2 + 3^2) = square root of (1+4+9) = square root of 14
np.linalg.norm(v1)
# square root of (4^2 + 5^2 + 6^2) = square root of (16+25+36) = square root of 14
np.linalg.norm(v2)
magnitude = np.linalg.norm(v1) * np.linalg.norm(v2)
print(magnitude)

result = dot_product / magnitude
print("result" , result)

from scipy import spatial

result1 = 1 - spatial.distance.cosine(v1, v2)

print("fonk result" , result1)