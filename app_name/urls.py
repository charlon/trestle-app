from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', '{{ app_name }}.views.example', name='example'),
    url(r'^test/', '{{ app_name }}.views.test', name='test'),
    
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    
    # include applications
    #url(r'^', include('app_name.urls')),
)
