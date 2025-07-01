from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    doing_date = models.DateField(null=True, blank=True)  # This field stores the date when the task needs to be done

    def __str__(self):
        return self.title
