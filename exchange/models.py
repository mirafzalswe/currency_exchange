from django.db import models

class History(models.Model):
    TransferFrom = models.CharField(max_length=100)
    TransferTo = models.CharField(max_length=100)
    amount = models.CharField(max_length=230)
    conversion_result = models.CharField(max_length=220)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.TransferFrom} to {self.TransferTo} ({self.date})"