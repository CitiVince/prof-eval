import datetime
from haystack import indexes
from evals.models import Professor, University, Comment


class UniversityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.CharField(model_attr='location')
    name_auto = indexes.EdgeNgramField(model_attr='name')
 
    def get_model(self):

        return University

    """
    def index_queryset(self):
        #Used when the entire index for model is updated.
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
   	"""