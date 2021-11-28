class Except(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


def exception(data):
    raise Except(data)
