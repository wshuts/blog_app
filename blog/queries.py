from pydantic import BaseModel

from blog.models import Article


class ListArticlesQuery:
    @staticmethod
    def execute():
        articles = Article.list()
        return articles


class GetArticleByIDQuery(BaseModel):
    article_id: str

    def execute(self) -> Article:
        return Article.get_by_id(self.article_id)
