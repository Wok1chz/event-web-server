from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Расписание', 'url_name': 'schedule'},
        {'title': 'Добавить мероприятие', 'url_name': 'addpage'},
]

class DataMixin:
        paginate_by = 3
        def get_user_context(self, **kwargs):
                context = kwargs
                context['data'] = EventUser.objects.all()
                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.pop(2)

                context['menu'] = user_menu
                # print(context)
                return context