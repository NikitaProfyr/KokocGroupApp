from django.db.models import Model


def get_dates(model: Model, **filters):
    return model.objects.filter(**filters).all()


def get_data(model: Model, **filters):
    return model.objects.get(**filters)



