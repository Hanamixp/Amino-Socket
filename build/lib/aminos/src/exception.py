class Except(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


def Exception(data):
    raise Except(data)
