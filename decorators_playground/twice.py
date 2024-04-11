def do_it_twice(f):
    def twice(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return twice
