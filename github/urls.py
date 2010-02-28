from django.conf.urls.defaults import *

urlpatterns = patterns('github.views',
    url(r'^$', 
        view='project_list', 
        name='project_index'
    ),
    url(r'^github-hook/(.+)/$',
        view='github_hook',
        name='project_github_hook'
    ),
    url(r'^(?P<project_slug>[\w-]+)/$', 
        view='project_detail', 
        name='project_detail'
    ),
    url(r'^(?P<project_slug>[\w-]+)/commits/$',
        view='commit_list',
        name='commit_list'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/$',
        view='blob_list', 
        name='blob_list'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/(?P<path>.+)/download/$', 
        view='blob_download',
        name='blob_download'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/(?P<path>.+)', 
        view='blob_detail',
        name='blob_detail'
    ),
)
