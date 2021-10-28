from django.db import models
import uuid

class internalTicket (models.Model):
    class Meta:
        verbose_name = "Internal Ticket"
        verbose_name_plural = "Internal Tickets"
    
    user_name = models.CharField(max_length=30)
    ticket_creation_date = models.DateTimeField('Problem Detected')
    subject_choices = [('INTERNAL PRODUCTION','Internal Production'),('ORDER FULFILLMENT', 'Order Fulfillment'),
    ('SHIPPING PROBLEMS', 'Shipping Problems'),('OTHER', 'Other')]
    subject = models.CharField(max_length=40, choices = subject_choices)
    description = models.TextField(max_length=1000)
    status_choices = [('OPEN','Open'),('BEING WORKED', 'Being Worked'),('CLOSED','Closed')]
    status = models.CharField(max_length=20, choices=status_choices, default="OPEN")
    ticket_resolution_date = models.DateTimeField('Problem Resolved', null=True)

    def __str__(self):
        return '%s\'s ticket about %s' % (self.user_name, self.subject)

class externalTicket (models.Model):
    class Meta:
        verbose_name = "External Ticket"
        verbose_name_plural = "External Tickets"
    
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=254)
    ticket_creation_date = models.DateField('Problem Detected')
    subject = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    status_choices = [('OPEN','Open'),('BEING WORKED', 'Being Worked'),('CLOSED','Closed')]
    status = models.CharField(max_length=20, choices=status_choices, default="OPEN")
    ticket_resolution_date = models.DateTimeField('Problem Resolved', null=True)

    def __str__(self):
        return '%s\'s ticket about %s' % (self.user_name, self.subject)