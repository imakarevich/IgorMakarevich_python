from django.shortcuts import render
from django.views import generic
from app_product_books.models import BookCard
import datetime
from django.db.models import Count

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "app_home_page/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
    
        #Days ago, when new book appeared
        td = datetime.timedelta(days=20)        
        objs_new = BookCard.objects.filter(date_entered_catalog__gt=datetime.date.today() - td)
        context['object_list'] = objs_new

        #
        book_names_set = set()
        book_authors_dict = dict()
        book_genres_dict = dict()
        book_years_of_publishing_dict = dict()
        book_covers_dict = dict()
        book_formats_dict = dict()
        book_age_restrictions_dict = dict() 
        book_publishings_dict = dict()

        objects_books = BookCard.objects.all()
        for book in objects_books:
            book_names_set.add(book.name)
            for authors in book.authors.all():
                book_authors_dict[authors.first_last_name] = authors.Book.all().count()
            for genre in book.genre.all():
                book_genres_dict[genre.name] = genre.Book.all().count()
            book_years_of_publishing_dict[book.year_of_publishing] = BookCard.objects.filter(year_of_publishing=book.year_of_publishing).count()
            book_covers_dict[book.cover] = BookCard.objects.filter(cover=book.cover).count()
            book_formats_dict[book.format] = BookCard.objects.filter(format=book.format).count()
            book_age_restrictions_dict[book.age_restrictions] = BookCard.objects.filter(age_restrictions=book.age_restrictions).count()
            for publishing in book.publishing.all():
                book_publishings_dict[publishing.name] = publishing.Book.all().count()

        data_for_accordion = {'Книги':sorted(book_names_set),
                            'Авторы':dict(sorted(book_authors_dict.items())),
                            'Издательство':dict(sorted(book_publishings_dict.items())),
                            'Жанры':dict(sorted(book_genres_dict.items())),
                            'Год издания':dict(sorted(book_years_of_publishing_dict.items())),
                            'Переплет':dict(sorted(book_covers_dict.items())),
                            'Формат':dict(sorted(book_formats_dict.items())),
                            'Возрастные ограничения':dict(sorted(book_age_restrictions_dict.items())),
                            }
        context['data_for_accordion'] = data_for_accordion

        # print(sorted(book_names_set),
        #                     dict(sorted(book_authors_dict.items())),
        #                     dict(sorted(book_genres_dict.items())),
        #                     dict(sorted(book_years_of_publishing_dict.items())),
        #                     dict(sorted(book_covers_dict.items())),
        #                     sorted(book_formats_set),
        #                     dict(sorted(book_age_restrictions_dict.items())), 
        #                     dict(sorted(book_publishings_dict.items()))
        #                     , sep='\n')

        # book_names_set_sorted_list = sorted(book_names_set)
        # book_authors_set_sorted_list = sorted(book_authors_set)
        # book_genres_set_sorted_list = sorted(book_genres_set)
        # book_years_of_publishing_set_sorted_list = sorted(book_years_of_publishing_set)
        # book_covers_set_sorted_list = sorted(book_covers_set)
        # book_formats_set_sorted_list = sorted(book_formats_set)
        # book_age_restrictions_set_sorted_list = sorted(book_age_restrictions_set) 
        # book_publishings_set_sorted_list = sorted(book_publishings_set)



            
        
        return context


