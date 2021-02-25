from django.db import models
from django.utils import timezone
# Create your models here.

# Requirements for the project (equivalent to business logic):
# - Tasks
#   - content
#   - creation_date
#   - deadline
#   - task_list
# - Other Features (optional)
#   - Status
#   - completed_on
# - task_list
#   - name


class TaskList(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    # Dunder Function
    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('IP', 'In Progress'),
        ('D', 'Dropped')
    )

    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[2], max_length=2)

    def __str__(self):
        return f"{self.content}.{self.task_list}"


