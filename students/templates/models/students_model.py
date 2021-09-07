from django.db import models


class Student(models.Model):
    """Student Model"""

    student_group = models.ForeignKey(
        'Group',
        verbose_name="Group",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='First name')

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Last name')

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Middle name',
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name='Birthday',
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name='Photo',
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Ticket')

    notes = models.TextField(
        blank=True,
        verbose_name='Notes')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """
        Return first_name plus last_name, with a space between
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()
