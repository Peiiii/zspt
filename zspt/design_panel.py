
class TableDesign:
    class users:
        id = ''
        username = ''
        avatar = ''
        introduction = ''
        registered_at = ''

    class user_auths:
        id = ''
        user_id = ''
        identity_type = ['username', 'phone', 'email']
        identifier = ''
        credential = ''

    class articles:
        id = ''
        author_id = ''
        title = ''
        summary = ''
        content = ''
        content_type = ['text/plain', 'text/html', 'text/markdown']
        content_text = ''
        created_at = ''
        updated_at = ''
        published_at = ''

    class comments:
        id = ''
        target_type = ['article', 'question', 'answer', 'collection', 'document', 'video', 'entry', '']
        target_id = ''
        author_id = ''
        parent_id = ''
        content = ''
        created_at = ''

    class polls:
        id = ''
        target_type = ['article', 'question', 'answer', 'collection', 'document', 'video']
        target_id = ''
        author_id = ''
        created_at = ''
        is_positive = ''

    class tags:
        id = ''
        name = ''
        articles = ''
        questions = ''
        answers = ''
        collections = ''
        documents = ''
        videos = ''

    class documents:
        pass

    class questions:
        pass

    class answers:
        pass
