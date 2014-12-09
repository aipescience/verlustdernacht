class Router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'lmdb':
            return 'lightcurve'

        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'lmdb':
            return 'lightcurve'

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'lmdb' or obj2._meta.app_label == 'lmdb':
           return True
        elif obj1._meta.app_label != 'lmdb' or obj2._meta.app_label != 'lmdb':
           return True
        return None

    def allow_migrate(self, db, model):
        if db == 'lmdb':
            return model._meta.app_label == 'lmdb'
        elif model._meta.app_label == 'lmdb':
            return False
        return None
