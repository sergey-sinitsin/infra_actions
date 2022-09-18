from django.http import HttpResponse


def index(request):
    return HttpResponse(f'У меня получилось! Выполнить деплой
    			f' через workflow. ))))')


def second_page(request):
    return HttpResponse('А это вторая страница!')
