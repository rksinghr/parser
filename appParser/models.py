from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class LocationType(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    name = models.CharField(max_length=50)
    locationType = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.locationType}"

class Frequency(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Config(models.Model):
    fileType = models.CharField(max_length=50)
    fullName = models.CharField(max_length=200)
    sourceFileLocation= models.CharField(max_length=200)
    sourceFileNamingConvention= models.CharField(max_length=200)
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE, default=1)
    outputSchemaName = models.CharField(max_length=200)
    outputObjectName = models.CharField(max_length=200)
    parser = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fileType}"

class ConfigLog(models.Model):
    sourceLogID = models.CharField(max_length=50)
    fileType = models.ForeignKey(Config, on_delete=models.CASCADE)
    sourceFile = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    dateExecuted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fileType}"