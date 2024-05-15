def provide(data: list[tuple]):
    def decorate(function):
        def wrap_function(*args, **kwargs):
            for provider in data:
                for value in provider:
                    args = args + (value,)
                function(*args, **kwargs)
        return wrap_function
    return decorate