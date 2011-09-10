from django.conf.urls.defaults import patterns
from dictionary.views import DictionaryListView, WordsListView

urlpatterns = patterns('',
    #...
    (r'^all/$', DictionaryListView()),
    (r'^(?P<entity_id>\d+)/words/$', WordsListView()),
)