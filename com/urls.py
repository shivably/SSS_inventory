from django.urls import path, include, re_path


from com.views import HomePageView
from com.views import LoginView
from com.views import LogoutView
from com.views import (
    CreateCustomer, CustomerTemplateView, CustomerUpdateView, CreateFeedBack)
from com.views import RegisterView, ReportsView
from com.api_views import DailySalesAPI, WeeklySalesAPI, MonthlySalesAPI


urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name='index'),
    re_path(r'^reports/$', ReportsView.as_view(), name='reports'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),

    # re_path(r'^api/', CreateCustomer.as_view(), name='create_customer'),

    re_path(r'^customer/create/$',
            CustomerTemplateView.as_view(), name='customers'),

    re_path(r'^customers/$', CreateFeedBack.as_view(),
            name='create_feedback'),
    re_path(r'^customer/(?P<pk>\d+)/update$',
            CustomerUpdateView.as_view(), name='update_customer'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^api/sales/daily/$', DailySalesAPI.as_view(),
            name='daily_sales_api'),
    re_path(r'^api/sales/weekly/$', WeeklySalesAPI.as_view(),
            name='weekly_sales_api'),
    re_path(r'^api/sales/monthly/$', MonthlySalesAPI.as_view(),
            name='monthly_sales_api'),
]
