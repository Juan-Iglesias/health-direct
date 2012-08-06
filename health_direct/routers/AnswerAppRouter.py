class AnswerAppRouter(object):

    def db_for_read(self, model, **hints):
        if model.__meta.app__label == 'AnswerApp' or model.__meta.app__label == 'QuestionBuilder':
            return 'answerapp'
        return None
        
    def db_for_write(self, model, **hints):
        if model.__meta.app__label == 'AnswerApp' or model.__meta.app__label == 'QuestionBuilder':
            return 'answerapp'
        return None
        
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1.__meta.app__label == 'AnswerApp' or obj1.__meta.app__label == 'QuestionBuilder') and (obj2.__meta.app__label == 'AnswerApp' or obj2.__meta.app__label == 'QuestionBuilder'):
            return True
        return None
        
    def allow_syncdb(self, db, model):
        if db == 'answerapp':
            return model.__meta.app__label == 'AnswerApp' or model.__meta.app__label == 'QuestionBuilder'
        elif model.__meta.app__label == 'AnswerApp' or model.__meta.app__label == 'QuestionBuilder':
            return False
        return None