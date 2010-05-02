def gen_rgb():
    for r in xrange(100):
        for g in xrange(100):
            for b in xrange(100):
                yield (r, g, b)

for rgb in gen_rgb():
    print rgb
