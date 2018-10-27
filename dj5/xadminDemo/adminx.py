


from .models import Article
from xadmin import site


class ArticleAdmin(object):
    model_icon = 'fa fa-home'


site.register(Article)

