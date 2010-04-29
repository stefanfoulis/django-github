from django.conf.urls.defaults import *

urlpatterns = patterns('github.views',
    url(r'^$', 
        view='project_list', 
        name='github_project_list'
    ),
    url(r'^github-hook/(.+)/$',
        view='github_hook',
        name='github_project_hook'
    ),
    url(r'^gists/$',
        view='gist_list',
        name='github_gist_list'
    ),
    url(r'^gists/(?P<gist_slug>[\w-]+)/$', 
        view='gist_detail', 
        name='github_gist_detail'
    ),
    url(r'^users/$',
        view='user_list',
        name='github_user_list'
    ),
    url(r'^users/(?P<login>[\w-]+)/$', 
        view='user_detail', 
        name='github_user_detail'
    ),
    url(r'^(?P<project_slug>[\w-]+)/$', 
        view='project_detail', 
        name='github_project_detail'
    ),
    url(r'^(?P<project_slug>[\w-]+)/commits/$',
        view='commit_list',
        name='github_commit_list'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/$',
        view='blob_list', 
        name='github_blob_list'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/(?P<path>.+)/download/$', 
        view='blob_download',
        name='github_blob_download'
    ),
    url(r'^(?P<project_slug>[\w-]+)/source/(?P<path>.+)', 
        view='blob_detail',
        name='github_blob_detail'
    ),
)
