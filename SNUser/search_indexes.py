from haystack import indexes
from SNUser.models import SNUser


class SNUserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    
    def get_model(self):
        return SNUser

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
