>>> output = []
    >>> for x in xrange(5):
    ...     output.append(str(x))
    ...
    >>> f = open('tmp.txt', 'w')
    >>> f.writelines(output)            # content is "01234"
    >>> f.writelines("\n".join(output)) # content is "012340\n1\n2\n3\n4"
    >>> f.close()