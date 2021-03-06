class BusinessCompaniesRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `datadrop_business`."""
        if model._meta.app_label == 'business_companies':
            return 'datadrop_business'
        return 'default'

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `datadrop_business`."""
        if model._meta.app_label == 'business_companies':
            return 'datadrop_business'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in this app.
        if obj1._meta.app_label == 'business_companies' and obj2._meta.app_label == 'business_companies':
            return True
        # No opinion if neither object is in this app (defer to default or other routers).
        elif 'business_companies' not in [
                obj1._meta.app_label, obj2._meta.app_label
        ]:
            return None
        # Allow for auth for the historical records which track
        # which user does an action
        elif 'business_companies' in [
                obj1._meta.app_label, obj2._meta.app_label
        ] and 'auth' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        # Block relationship if one object is in the Example app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'business_companies':
            # The Example app should be migrated only on the datadrop_business database.
            return db == 'datadrop_business'
        elif db == 'datadrop_business':
            # Ensure that all other apps don't get migrated on the datadrop_business database.
            return False

        # No opinion for all other scenarios
        return None
