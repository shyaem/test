from django.forms import ModelForm
from articles.models import Article

class CreateArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug','body','thumb']
