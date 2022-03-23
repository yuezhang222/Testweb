from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.utils.translation import gettext_lazy as _

class Caselist(models.Model):

    user_name = models.CharField(max_length=30,verbose_name=_('用户名'))
    iterm = models.CharField(max_length=30)
    release = models.CharField(max_length=30)
    modules = models.CharField(max_length=30)
    case_name = models.CharField(max_length=100,verbose_name=_('测试用例名称'))
    case_id = models.AutoField(primary_key=True)
    case_time = models.DateTimeField(auto_now_add=True)
    upload_py = models.FileField(upload_to='./testapi/case/',unique=True)
    upload_json = models.FileField(upload_to='./testapi/case/',unique=True)
    upload_run = models.FileField(upload_to='./testapi/case/',unique=True,verbose_name=_('运行文件'),help_text=u'用来运行的文件')
    upload_core = models.FileField(upload_to='./testapi/case/',unique=True)
    case_status = models.BooleanField('Execution status',default=True,)

    # def Caselist_filter(request):
    #     k = models.Caselist.objects.get(case_id=a.case_id)
    #     case_id=request.get
    #     if Caselist.report_url.get
    #         models.Caselist.objects.get(case_id)

    class  Meta:
        verbose_name = _('case')
        verbose_name_plural = _('caselist')


class Reportbase(models.Model):

    user_name = models.CharField(max_length=30,verbose_name=_('用户名'))
    iterm = models.CharField(max_length=30)
    release = models.CharField(max_length=30)
    modules = models.CharField(max_length=30)
    report_name = models.CharField(max_length=100,verbose_name=_('报告名称'))
    report_id = models.AutoField(primary_key=True,verbose_name=_('报告ID'))
    report_url= models.CharField(max_length=300,verbose_name=_('报告地址'))
    report_time = models.DateTimeField(auto_now_add=True,verbose_name=_('报告时间'))


    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reportlist')




class  Relyon(models.Model):

    tool_name = models.CharField(max_length=100)
    tool_id = models.AutoField(primary_key=True)
    upload_py= models.FileField(upload_to='./testapi/case/',unique=True)
    tool_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Relyon')
        verbose_name_plural = _('依赖文件')


# class  Mock_server(models.Model):
#     '''
#     mitprxoy
#     '''
#     mock_name = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = _('MOCK')
#         verbose_name_plural = _('Mock_Server')


