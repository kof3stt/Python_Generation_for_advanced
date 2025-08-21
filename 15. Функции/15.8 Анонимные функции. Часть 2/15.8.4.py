is_num = (
    lambda s: s[1:].count("-") == 0
    and s.replace(".", "", 1).replace("-", "", 1).isdigit()
)
