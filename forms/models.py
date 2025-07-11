from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    # Fields inside "fields" key in the request
    treadDiameterNew = models.CharField(max_length=100)
    lastShopIssueSize = models.CharField(max_length=100)
    condemningDia = models.CharField(max_length=100)
    wheelGauge = models.CharField(max_length=100)
    variationSameAxle = models.CharField(max_length=100)
    variationSameBogie = models.CharField(max_length=100)
    variationSameCoach = models.CharField(max_length=100)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=100)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)

    status = models.CharField(max_length=20, default='Saved')

    def __str__(self):
        return self.formNumber
