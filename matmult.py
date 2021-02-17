# Program to multiply two matrices using numpy instead
import numpy

N = 25

X = numpy.random.randint(0,100,(N,N))
Y = numpy.random.randint(0,100,(N,N+1))
result = numpy.dot(X,Y)
print(result)
