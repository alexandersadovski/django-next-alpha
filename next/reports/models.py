from django.contrib.auth import get_user_model
from django.db import models
from next.reports.choices import ReasonChoices


class Report(models.Model):
    reported_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='reports_made',
    )
    reported_user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='reports_received',
    )
    reason = models.CharField(
        max_length=25,
        choices=ReasonChoices.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    status = models.CharField(
        max_length=25,
    )
