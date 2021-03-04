from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None)

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('IP', 'In Progress'),
        ('D', 'Dropped')
    )

    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[2], max_length=2)

    def __str__(self):
        return f"{self.content}.{self.task_list}"
