# frontend/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from frontend.models import Schoolclasses
from .models import Mark

@receiver(post_save, sender=Schoolclasses)
def create_marks_model(sender, instance, created, **kwargs):
    if created:
        class_name = instance
        subjects = class_name.subjects.all()

        for subject in subjects:
            Mark.objects.create(class_name=class_name, subject=subject)
