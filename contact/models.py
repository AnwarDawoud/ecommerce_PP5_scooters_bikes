from django.db import models


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'

    name = models.CharField(max_length=254)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.subject} from {self.name}"
