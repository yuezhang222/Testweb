from django.db import models

from django.utils.translation import gettext_lazy as _

class  Mock_server(models.Model):
    '''
    mitprx
    '''
    user_name = models.CharField(max_length=100)
    mock_name = models.CharField(max_length=100)
    mock_response=models.JSONField(null=True,blank=True)
    mock_http=models.CharField(max_length=100)
    mock_path = models.CharField(max_length=100)
    old_response = models.TextField(null=True,blank=True,default=None)
    mock_status = models.BooleanField('Execution status',default=True,)

    class Meta:
        verbose_name = _('MOCK')
        verbose_name_plural = _('Mock_sever')
