
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from json import loads
from django.http import HttpResponse
import io
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from reportlab.pdfgen import canvas

from .forms import *
from .models import *
from .utils import *



class EventHome(DataMixin, ListView):
    model = Event
    template_name = 'event/schedule.html'
    context_object_name = 'posts'
    data = EventUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расписание")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Event.objects.filter(is_published=True)


class ShowProfile(DataMixin, ListView):
    model = EventUser
    template_name = 'event/profile.html'
    context_object_name = 'events'
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Личный кабинет")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Event
    template_name = 'event/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

def index(request):
    return render(request, 'event/index.html', {'menu': menu, 'title': 'Главная страница'})

# def schedule(request):
#     posts = Event.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Список мероприятий'
#     }
#     return render(request, 'event/schedule.html', context=context)

class AddPage(LoginRequiredMixin, DataMixin,CreateView):
    form_class = AddEventForm
    template_name = 'event/addpage.html'
    login_url = reverse_lazy('home')
    # pk_url_kwarg = 'user_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить мероприятие")
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddEventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#             form = AddEventForm()
#     return render(request, 'event/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление мероприятия'})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'event/register.html'
    success_url = reverse_lazy('login')
    #
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'event/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


#
# def profile(request):
#     return render(request, 'event/profile.html', {'menu': menu, 'title': 'Личный кабинет'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

def logout_user(request):
    logout(request)
    return redirect('login')

def event_sign(request):
    print(request.POST)
    if (len(EventUser.objects.filter(user_id=request.POST.get('userId'))) >= 1) and (len(EventUser.objects.filter(event_id=request.POST.get('postId'))) >= 1):
        print('Такие записи уже есть')
    else:
        data = EventUser()
        data.user_id = request.POST.get('userId')
        data.event_id = request.POST.get('postId')
        data.save()

    return HttpResponse("POST request")

def event_delete(request):
    print(request.POST)
    user_id = request.POST.get('userId')
    post_id = request.POST.get('postId')
    data = EventUser.objects.filter(user_id=user_id, event_id=post_id)
    data.delete()
    return HttpResponse("POST request")


def get_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    print(p)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

