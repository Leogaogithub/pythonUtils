#https://pypi.org/project/python-amazon-product-api/

from amazonproduct import API
api = API(locale='us')


# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)