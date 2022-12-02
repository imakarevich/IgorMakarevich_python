from django.shortcuts import render
from django.views import generic
from app_product_books.models import BookCard
from app_reference_book.models import Authors, PublishingHouse, Genres
import datetime
from django.db.models import Q


# Create your views here.
def get_data_for_accordion():
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

    return data_for_accordion   

def get_objects_bookcard_name(accordion_position_list):
            if accordion_position_list:
                objects = []
                for pos in accordion_position_list:
                    objects += BookCard.objects.filter(name=pos)
                return objects
            else:
                return []

#custom functions
def get_objects_bookcard_authors(accordion_position_list):
            if accordion_position_list:
                objects = []
                objects_book_list = []
                for pos in accordion_position_list:
                    objects += Authors.objects.filter(first_last_name=pos)
                for obj in objects:
                    objects_book_list += obj.Book.all() 
                return objects_book_list
            else:
                return []
def get_objects_bookcard_publishing(accordion_position_list):
            if accordion_position_list:
                objects = []
                objects_book_list = []
                for pos in accordion_position_list:
                    objects += PublishingHouse.objects.filter(name=pos)
                for obj in objects:
                    objects_book_list += obj.Book.all() 
                return objects_book_list
            else:
                return []
def get_objects_bookcard_genre(accordion_position_list):
            if accordion_position_list:
                objects = []
                objects_book_list = []
                for pos in accordion_position_list:
                    objects += Genres.objects.filter(name=pos)
                for obj in objects:
                    objects_book_list += obj.Book.all() 
                return objects_book_list
            else:
                return []
def get_objects_bookcard_year_of_publishing(accordion_position_list):
            if accordion_position_list:
                objects = []
                for pos in accordion_position_list:
                    objects += BookCard.objects.filter(year_of_publishing=pos)
                return objects
            else:
                return []
def get_objects_bookcard_cover(accordion_position_list):
            if accordion_position_list:
                objects = []
                for pos in accordion_position_list:
                    objects += BookCard.objects.filter(cover=pos)
                return objects
            else:
                return []
def get_objects_bookcard_format(accordion_position_list):
            if accordion_position_list:
                objects = []
                for pos in accordion_position_list:
                    objects += BookCard.objects.filter(format=pos)
                return objects
            else:
                return []
def get_objects_bookcard_age_restrictions(accordion_position_list):
            if accordion_position_list:
                objects = []
                for pos in accordion_position_list:
                    objects += BookCard.objects.filter(age_restrictions=pos)
                return objects
            else:
                return []

#view functions and classes
class HomePage(generic.TemplateView):
    template_name = "app_home_page/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
    
        #Days ago, when new book appeared
        td = datetime.timedelta(days=20)        
        objs_new = BookCard.objects.filter(date_entered_catalog__gt=datetime.date.today() - td)
        context['object_list'] = objs_new
        context['data_for_accordion'] = get_data_for_accordion()

        #
        # book_names_set = set()
        # book_authors_dict = dict()
        # book_genres_dict = dict()
        # book_years_of_publishing_dict = dict()
        # book_covers_dict = dict()
        # book_formats_dict = dict()
        # book_age_restrictions_dict = dict() 
        # book_publishings_dict = dict()

        # objects_books = BookCard.objects.all()
        # for book in objects_books:
        #     book_names_set.add(book.name)
        #     for authors in book.authors.all():
        #         book_authors_dict[authors.first_last_name] = authors.Book.all().count()
        #     for genre in book.genre.all():
        #         book_genres_dict[genre.name] = genre.Book.all().count()
        #     book_years_of_publishing_dict[book.year_of_publishing] = BookCard.objects.filter(year_of_publishing=book.year_of_publishing).count()
        #     book_covers_dict[book.cover] = BookCard.objects.filter(cover=book.cover).count()
        #     book_formats_dict[book.format] = BookCard.objects.filter(format=book.format).count()
        #     book_age_restrictions_dict[book.age_restrictions] = BookCard.objects.filter(age_restrictions=book.age_restrictions).count()
        #     for publishing in book.publishing.all():
        #         book_publishings_dict[publishing.name] = publishing.Book.all().count()

        # data_for_accordion = {'Книги':sorted(book_names_set),
        #                     'Авторы':dict(sorted(book_authors_dict.items())),
        #                     'Издательство':dict(sorted(book_publishings_dict.items())),
        #                     'Жанры':dict(sorted(book_genres_dict.items())),
        #                     'Год издания':dict(sorted(book_years_of_publishing_dict.items())),
        #                     'Переплет':dict(sorted(book_covers_dict.items())),
        #                     'Формат':dict(sorted(book_formats_dict.items())),
        #                     'Возрастные ограничения':dict(sorted(book_age_restrictions_dict.items())),
        #                     }
        # context['data_for_accordion'] = data_for_accordion
        return context
    
def search_from_accordion(request):
    context = {}
    object_list = []
    for_checked_atribute_input = []
    context['data_for_accordion'] = get_data_for_accordion()
    if request.method == "GET":
        accordion_position_1 = request.GET.getlist('accordion_position_1[]')
        accordion_position_2 = request.GET.getlist('accordion_position_2[]')
        accordion_position_3 = request.GET.getlist('accordion_position_3[]')
        accordion_position_4 = request.GET.getlist('accordion_position_4[]')
        accordion_position_5 = request.GET.getlist('accordion_position_5[]')
        accordion_position_6 = request.GET.getlist('accordion_position_6[]')
        accordion_position_7 = request.GET.getlist('accordion_position_7[]')
        accordion_position_8 = request.GET.getlist('accordion_position_8[]')

        accordion_position_5_int = []
        for i in accordion_position_5:
            accordion_position_5_int.append(int(i))

        for_checked_atribute_input.extend(accordion_position_1)
        for_checked_atribute_input.extend(accordion_position_2)
        for_checked_atribute_input.extend(accordion_position_3)
        for_checked_atribute_input.extend(accordion_position_4)
        for_checked_atribute_input.extend(accordion_position_5_int)
        for_checked_atribute_input.extend(accordion_position_6)
        for_checked_atribute_input.extend(accordion_position_7)
        for_checked_atribute_input.extend(accordion_position_8)

        object_list.extend(get_objects_bookcard_name(accordion_position_1))
        object_list.extend(get_objects_bookcard_authors(accordion_position_2))
        object_list.extend(get_objects_bookcard_publishing(accordion_position_3))
        object_list.extend(get_objects_bookcard_genre(accordion_position_4))
        object_list.extend(get_objects_bookcard_year_of_publishing(accordion_position_5))
        object_list.extend(get_objects_bookcard_cover(accordion_position_6))
        object_list.extend(get_objects_bookcard_format(accordion_position_7))
        object_list.extend(get_objects_bookcard_age_restrictions(accordion_position_8))

        object_list = set(object_list)

        print(object_list)
        
        print(accordion_position_1, accordion_position_2, accordion_position_3, accordion_position_4,accordion_position_5,accordion_position_6, accordion_position_7, accordion_position_8, sep='\n')

        context['for_checked_atribute_input'] = for_checked_atribute_input
        context['object_list'] = object_list

        print('12321', for_checked_atribute_input)

    return render(
        request=request,
        template_name='app_home_page/search_from_accordion.html',
        context=context
    )





