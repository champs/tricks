s = "Hi Sivasrinivas, your Uber is arriving now!"


def splitstr(s, l=25):
    """ split string with max length < l
            "(i/n)"
    """
    arr = [len(x) for x in s.split()]
    out = []
    counter = 5
    tmp_out = ''
    for i in xrange(len(arr)):
        if counter + arr[i] > l:
            out.append(tmp_out)
            tmp_out = ''
            counter = 5
        else:
            tmp_out += s.split()[i] + ' '
            counter = len(tmp_out) + 5

    return out

print splitstr(s)
print[len(x) for x in splitstr(s)]
