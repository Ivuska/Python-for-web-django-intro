from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

# Tato metoda zajistuje, ze se mi i v admin rozhrani na seznamu polozek
# daneho objektu a take pri vyberu z kategorii dobrazuje nazev kurzu,
# nikoli napr. category object (1).
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Branch(models.Model):
    city = models.CharField(max_length=50)
    initial_date = models.DateField()
    email = models.EmailField(max_length=80)
    number_of_employees = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self) -> str:
        return self.city
    
    def courses_list(self):
        return Course.objects.filter(branch=self)

class Person(models.Model):
    name_and_surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    position = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name_and_surname

class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='lecturer')
    event_coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True,related_name='event_coordinator')

    def __str__(self) -> str:
        return self.name

class Application(models.Model):
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    motivation = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.surname + ' ' + self.first_name