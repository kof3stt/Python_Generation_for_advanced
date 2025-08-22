words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik", "beegeek"]

result = {key: [ord(i) for i in key] for key in words}
