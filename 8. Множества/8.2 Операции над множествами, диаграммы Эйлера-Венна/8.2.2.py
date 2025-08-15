# Книги на прочтение 📚🌶️
n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
one_book = x + y + t - m - n - k + y + z + t - m - n - k + x + z + t - m - n - k
two_books = n + m - x - t + k + m - y - t + n + k - z - t
zero_books = a - one_book - two_books - t
print(one_book, two_books, zero_books, sep="\n")
