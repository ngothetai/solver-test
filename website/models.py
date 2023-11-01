from django.db import models
from mdeditor.fields import MDTextField

class problem(models.Model):
    problemID = models.CharField(max_length=255, primary_key=True)
    problemName = models.CharField(max_length=255)
    description = models.TextField()
    # Store image in sqlite by binary type
    image1 = models.BinaryField(null=True, blank=True)
    image2 = models.BinaryField(null=True, blank=True)
    image3 = models.BinaryField(null=True, blank=True)
    principles = models.TextField()
    dataDescription = models.TextField()
    parameterDescription = models.TextField()
    programDescription = models.TextField()
    solutionDescription = models.TextField()
    codePython = models.TextField()
    codeC = models.TextField()
    codeJava = models.TextField()
    date = models.DateField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.problemName
    
class model(models.Model):
    modelID = models.CharField(max_length=255, primary_key=True)
    modelName = models.CharField(max_length=255)
    problemID = models.ForeignKey(problem, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    principal = models.CharField(max_length=255)
    advanced = models.BooleanField()
    date = models.DateField()
    status = models.CharField(max_length=255)
    isActive = models.BooleanField()

    def __str__(self):
        return self.modelName

    
class example(models.Model):
    exampleID = models.CharField(max_length=255, primary_key=True)
    exampleName = models.CharField(max_length=255)
    inputFile = models.FileField(upload_to='example_files/')
    maxIteration = models.IntegerField()
    maxTime = models.TimeField()
    description = models.TextField()
    image = models.BinaryField(null=True, blank=True)
    modelID = models.ForeignKey(model, on_delete=models.CASCADE)
    date = models.DateField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.exampleName
    
class example_run(models.Model):
    STATUS_EXAMPLE_CHOICES = [
        ('completed', 'Hoàn thành'),
        ('incomplete', 'Chưa hoàn thành'),
        ('pending', 'Chờ xử lý'),
        ('processing', 'Đang xử lý'),
        ('error', 'Lỗi'),
        ('success', 'Thành công'),
    ]
    runID = models.CharField(max_length=255, primary_key=True)
    exampleID = models.ForeignKey(example, on_delete=models.CASCADE)
    userName = models.CharField(max_length=255)
    runDateTime = models.DateTimeField(auto_now_add=True)
    runStatus = models.CharField(max_length=20, choices=STATUS_EXAMPLE_CHOICES)
    paramList = models.JSONField()

    def __str__(self):
        return self.exampleName
    
class solver(models.Model):
    solverID = models.CharField(max_length=255, primary_key=True)
    solverName = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    strengths = models.TextField(max_length=255)
    applications = models.TextField(max_length=255)
    referencesURL = models.URLField(max_length=255)
    date = models.DateField()
    isActive = models.BooleanField()
    
    def __str__(self) -> str:
        return self.solverName
    
class model_run(models.Model):
    runID = models.CharField(max_length=255, primary_key=True)
    modelID = models.ForeignKey(model, on_delete=models.CASCADE)
    userName = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)
    outputFile = models.FileField(upload_to='output_model_run/')
    solverID = models.ForeignKey(solver, on_delete=models.CASCADE)
    date = models.DateField()
    isActive = models.BooleanField()


class param_run(models.Model):
    runID = models.OneToOneField(model_run, on_delete=models.CASCADE, primary_key=True)
    param = models.JSONField()
    # Con mot vai thuoc tinh chua ro
    isActive = models.BooleanField()

class default_param(models.Model):
    solverID = models.OneToOneField(solver, on_delete=models.CASCADE, primary_key=True)
    paramName = models.TextField(max_length=255)
    disValue = models.TextField(max_length=255)
    conValue = models.TextField(max_length=255)
    editable = models.BooleanField()
    isActive = models.BooleanField()
    
    def __str__(self) -> str:
        return self.paramName
    
class model_solver(models.Model):
    modelID = models.ForeignKey(model, on_delete=models.CASCADE)
    solverID = models.ForeignKey(solver, on_delete=models.CASCADE)


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()