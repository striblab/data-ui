class BusinessCompaniesRouter(object):
    """
    A router to control all database operations on models in
    the this application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on business_companies models to 'datadrop_business'
        """
        if model._meta.app_label == 'business_companies':
            return 'datadrop_business'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on business_companies models to 'other'
        """
        if model._meta.app_label == 'business_companies':
            return 'datadrop_business'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the 'business_companies' app only appears on the 'other' db
        """
        if db == 'datadrop_business':
            return model._meta.app_label == 'business_companies'
        elif model._meta.app_label == 'business_companies':
            return False
        return None
