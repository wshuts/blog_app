from blog.models import Article


class ListArticlesQuery:
    @staticmethod
    def execute():
        articles = Article.list()
        return articles
