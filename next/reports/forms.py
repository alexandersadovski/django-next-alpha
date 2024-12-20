from django import forms
from next.reports.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
