from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.home', name='home'),
    url(r'^login/', 'qa.views.test', name='login'),
    url(r'^signup/', 'qa.views.test', name='signup'),
    url(r'^question/(?P<qn>\d+)/$', 'qa.views.show_question', name='question'),
    url(r'^ask/', 'qa.views.question_add', name='ask'),
    url(r'^popular/', 'qa.views.show_popular', name='popular'),
    url(r'^new/', 'qa.views.test', name='new'),
)
