from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RawData


@csrf_exempt
def notSpecificData(request):
    data = request.body.decode('utf-8')
    if len(data) == 0:
        return HttpResponse('<h1>Thanks, but no data was saved :)<h1>')

    RawData.objects.create(data=request.body, tag="notSpecificData", main="")
    return HttpResponse('<h1>Saved, thanks :)<h1>')
