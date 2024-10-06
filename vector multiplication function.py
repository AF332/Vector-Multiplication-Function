def vector_multipication(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    result = []

    for i in range(len(vector1)):
        result.append(vector1[i] * vector2[i]) # Iterates over the elements of both vectors and multiples them.

    return result

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

result = vector_multipication(vector1, vector2)
print(f"Results of vector multiplication: {result}")