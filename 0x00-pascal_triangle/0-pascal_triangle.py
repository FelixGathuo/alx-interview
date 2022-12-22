def pascal_triangle_generator():
    la=[1]
    while True:
        for i in la:
            yield i
        yield None
        lb=[1]
        lb.extend(i+j for i, j in zip(la[:-1], la[1:]))
        lb.append(1)
        la=lb
