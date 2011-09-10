# Create your views here.
from django import http
from django.views.generic.list import ListView
from common.views import JSONResponseMixin
from dictionary.models import Dictionary, GeoLocationType
from django.utils import simplejson as json

class DictionaryListView(object):

    def __call__(self, request):

        if request.GET.get('tags'):
            tags = request.GET.get('tags').split(',')
            types = [t.pk for t in GeoLocationType.objects.filter(type__in=tags)]
            dicts = Dictionary.objects.filter(types__id__in=types)
        else:
            dicts = Dictionary.objects.all()

        json_data = [prop.to_dict() for prop in dicts]
        return http.HttpResponse(json.dumps(json_data),
                                 content_type='application/json')


class WordsListView(object):
    model = Dictionary

    def __call__(self, request, entity_id):
        words = Dictionary.objects.get(pk=entity_id).word_set.all()
        json_data = [prop.to_dict() for prop in words]
        return http.HttpResponse(json.dumps(json_data),
                                 content_type='application/json')

