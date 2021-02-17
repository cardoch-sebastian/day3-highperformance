import numpy

if __name__ == '__main__':
    a = numpy.empty(10)
    a[:] = numpy.NaN
    a[5] = 1
    print(a)

    b = numpy.arange(10,50)
    print(b)

    c = numpy.arange(20)
    c = c[::-1]
    print(c)

    d = numpy.random.randint(0,8,(3,3))
    print(d)

    e = numpy.array([1,2,0,0,4,0])
    indices = numpy.where(e==0)[0]
    print(indices)

    f = numpy.random.rand(30)
    mean = numpy.average(f)
    print(mean)

    g = numpy.ones((5,5))
    g[1:-1, 1:-1] = 0
    print(g)

    h = numpy.ones((8,8))
    h[0::2,0::2] = 0
    h[1::2,1::2] = 0
    print(h)

    i = numpy.tile([[1,0],[0,1]],(4,4))
    print(i)

    j = numpy.arange(11)
    jb = ~numpy.isin(j,numpy.arange(3,9))
    print(j)
    print(jb)

    k = numpy.random.random(10)
    k.sort()
    print(k)

    A = numpy.random.randint(0,2,5)
    B = numpy.random.randint(0,2,5)
    l = numpy.array_equal(A,B)
    print(l)

    m = numpy.arange(10, dtype=numpy.int32)
    print(m.dtype)
    m = m.astype('int64')
    print(m.dtype)

    A = numpy.arange(9).reshape(3,3)
    B = A + 1
    C = numpy.dot(A,B)
    D = numpy.diag(C)
    print(D)

    



    