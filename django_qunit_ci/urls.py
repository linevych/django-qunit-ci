from django.conf.urls.defaults import patterns

# This should be safe to leave in the URL configuration even in production;
# the view always returns a 404 if the test classes haven't been loaded

urlpatterns = patterns('django_qunit_ci.views',
    (r'^django_qunit_ci_test/$', 'run_qunit_tests', {}, 'django-qunit-ci-test')
)
