from django.utils import timezone
from myapp.models import Author, Genre, Book

author1 = Author.objects.create(first_name='Стивен', last_name='Кинг', biography='Знаменитый американский писатель, получивший титул Короля ужасов')
author2 = Author.objects.create(first_name='Франк', last_name='Тилье', biography='Французский автор жестких триллеров и детективов.')

genre1 = Genre.objects.create(name='Ужасы', description='Жанр, призванный вызывать чувство страха и напряжения.')
genre2 = Genre.objects.create(name='Детектив', description='В произведениях этого жанра всегда есть тайны, связанные с преступлениями.')

book1 = Book.objects.create(title='Мизери', description='Популярный писатель попадает в руки сумасшедшей поклонницы.', publication_date=timezone.now(), num_pages=380, price=560.00, author=author1, is_bestseller=True)
book1.genres.add(genre1)

book2 = Book.objects.create(title='Головокружение', description='Трое незнакомых друг с другом людей приходят в себя в ледяной пещере.', publication_date=timezone.now(), num_pages=370, price=440.00, author=author2, is_bestseller=True)
book2.genres.add(genre2)
