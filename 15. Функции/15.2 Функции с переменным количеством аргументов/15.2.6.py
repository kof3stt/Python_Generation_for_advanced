def info_kwargs(**kwargs):
    for key in sorted(kwargs):
        print(key + ":", kwargs[key])
