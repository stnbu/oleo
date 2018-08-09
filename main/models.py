from django.db import models

class Page(models.Model):
    weight = models.FloatField(default=0.0)
    name = models.CharField(max_length=30)
    label = models.CharField(max_length=60)
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    main = models.TextField(blank=True)

    def __str__(self):
        return self.page.name
