def identity(*args, **kwargs):
    return args, kwargs


def decorator_identity(*_args, **_kwargs):
    return identity
