import uuid, time, enum, contextlib
from sqlalchemy import Column, Integer, Text, String, DateTime, Sequence, Date, Boolean, Float, ForeignKey, Enum, \
    PickleType
from sqlalchemy.ext.declarative import declared_attr
from web import sql,StateManger
from zspt.utils import generate_random_id, generate_hash
Model=sql.Model
BaseMixin=sql.BaseMixin

class IdentityType(enum.Enum):
    user_name = 1
    phone = 2
    email = 3
    qq = 4
    wechat = 5
    weibo = 6


class ArticleContentType(enum.Enum):
    text_plain = 1
    text_html = 2
    text_markdown = 3


class SiteContentType(enum.Enum):
    article = 1
    document = 2
    collection = 3
    entry = 4
    video = 5
    question = 6
    answer = 7
    knowledge_card = 8
    mind_map = 9
    note = 10






class User(BaseMixin, Model):
    __tablename__ = 'users'
    id = sql.Column(sql.String(80), primary_key=True, default=generate_random_id, nullable=False)
    username = sql.Column(sql.String(80), unique=True, default=lambda: '用户' + uuid.uuid4().hex)
    avatar = sql.Column(sql.String(80))
    gender = sql.Column(sql.String(10))
    introduction = sql.Column(sql.String(500))
    registered_at = sql.Column(sql.Float, default=lambda: time.time())

    def auto_fill(self):
        if not self.id:
            self.id = generate_random_id()
        if not self.avatar:
            self.avatar = 'http://www.gravatar.com/avatar/%s?s=256&d=retro' % (generate_hash(self.id))
        return self


class UserAuth(BaseMixin, Model):
    __tablename__ = 'user_auths'
    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    user_id = Column(String(80), ForeignKey('users.id'), nullable=False)
    identity_type = Column(Enum(IdentityType))
    identifier = Column(String(80), unique=True)
    credential = Column(String(80))


class AssetMixin(BaseMixin):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    created_at = Column(Float, default=time.time, nullable=False)

    @declared_attr
    def author_id(cls):
        return Column(String(80), ForeignKey('users.id', ondelete='SET NULL'))


class ContentMixin(AssetMixin):
    title = Column(Text, nullable=False)
    introduction = sql.Column(sql.String(500))
    updated_at = Column(Float)
    published_at = Column(Float)
    category = Column(String(80))
    likes = Column(Integer)
    dislikes = Column(Integer)
    views = Column(Integer)
    state = Column(String(80))


class Article(ContentMixin, Model):
    __tablename__ = 'articles'

    summary = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    content_type = Column(Enum(ArticleContentType), nullable=False)
    content_text = Column(Text)
    content_html = Column(Text)
    content_markdown = Column(Text)


class Draft(ContentMixin, Model):
    __tablename__ = 'drafts'

    summary = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    content_type = Column(Enum(ArticleContentType), nullable=False)
    content_text = Column(Text)
    content_html = Column(Text)
    content_markdown = Column(Text)


class Document(ContentMixin, Model):
    __tablename__ = 'documents'

    filename = Column(String(80))
    uploaded_at = Column(Float, default=time.time)
    mime_type = Column(String(80))


class Entry(ContentMixin, Model):
    __tablename__ = 'entries'
    author_id = Column(String(80), ForeignKey('users.id', ondelete='SET NULL'))
    introduction = Column(String(500))
    content = Column(Text)


class Video(ContentMixin, Model):
    __tablename__ = 'videos'
    filename = Column(String(80))


class KnowledgeCard(ContentMixin, Model):
    __tablename__ = 'knowledge_cards'
    content = Column(Text)


class MindMap(ContentMixin, Model):
    __tablename__ = 'mind_maps'
    content = Column(Text)


class Note(ContentMixin, Model):
    __tablename__ = 'notes'
    content = Column(Text)


class Collection(ContentMixin, Model):
    __tablename__ = 'collections'
    content = Column(PickleType, default=[])


class Collection2Content(Model):
    __tablename__ = 'collection2content'
    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    collection_id = Column(String(80), ForeignKey('collections.id', ondelete='CASCADE'))
    content_id = Column(String(80))


class Question(ContentMixin, Model):
    __tablename__ = 'questions'
    content = Column(Text)


class Answer(ContentMixin, Model):
    __tablename__ = 'answers'
    content = Column(Text)


class Comment(AssetMixin, Model):
    __tablename__ = 'comments'
    target_type = Column(Enum(SiteContentType))
    target_id = Column(String(80), nullable=False)
    reference_id = Column(String(80))
    content = Column(Text)


class Poll(AssetMixin, Model):
    __tablename__ = 'polls'
    target_type = Column(Enum(SiteContentType))
    target_id = Column(String(80), nullable=False)
    is_positive = Column(Boolean)


class Category(BaseMixin,Model):
    __tablename__ = 'categories'
    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    name = Column(String(80), nullable=False)


class Tag(BaseMixin,Model):
    __tablename__ = 'tags'
    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    name = Column(String(80), nullable=False)


class Content2Tag(BaseMixin,Model):
    __tablename__ = 'content2tags'
    id = Column(String(80), primary_key=True, default=generate_random_id, nullable=False)
    content_id = Column(String(80), nullable=False)
    tag_id = Column(String(80), ForeignKey('tags.id'), nullable=False)
