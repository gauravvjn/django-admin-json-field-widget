from django.db import models
from django.contrib.postgres.fields import JSONField


class TestModel(models.Model):
    json_field = JSONField(null=True, blank=True)
