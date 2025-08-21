def ignore_command(command):
    ignore = [
        "alias",
        "configuration",
        "ip",
        "sql",
        "select",
        "update",
        "exec",
        "del",
        "truncate",
    ]
    return any(map(lambda s: s in command, ignore))
