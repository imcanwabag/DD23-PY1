PAGES_PER_BOOK = 100
LINES_PER_PAGE = 50
CHARS_PER_LINE = 25
BYTES_PER_CHAR = 4

MEMORY_PER_BOOK = PAGES_PER_BOOK * LINES_PER_PAGE * \
                  CHARS_PER_LINE * BYTES_PER_CHAR
AVAILABLE_MEMORY = 1.44 * (1024 * 1024)

books_count = int(AVAILABLE_MEMORY // MEMORY_PER_BOOK)

print("Количество книг, помещающихся на дискету:", books_count)
