from unittest.mock import Mock

from django.http import HttpResponseRedirect
from django.test import SimpleTestCase
from django.test.utils import override_settings

from nose.tools import eq_, ok_

from masterfirefoxos.base.tests import TEST_VERSIONS_LOCALE_MAP
from masterfirefoxos.base.middleware import NonExistentLocaleRedirectionMiddleware


class TestNonExistentLocaleRedirectionMiddleware(SimpleTestCase):
    def setUp(self):
        self.middleware = NonExistentLocaleRedirectionMiddleware()

    def test_user_authenticated(self):
        request = Mock()
        request.user.is_authenticated.return_value = True
        eq_(self.middleware.process_request(request), None)

    def test_path_starts_with_en(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path.startswith.return_value = '/en/foo-bar'
        eq_(self.middleware.process_request(request), None)

    @override_settings(VERSIONS_LOCALE_MAP=TEST_VERSIONS_LOCALE_MAP)
    def test_locale_for_version_exists(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path = '/xx/version-90'
        eq_(self.middleware.process_request(request), None)

    @override_settings(VERSIONS_LOCALE_MAP=TEST_VERSIONS_LOCALE_MAP)
    def test_locale_for_version_does_not_exist(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path = '/xx/version-100t/demo-tips'
        response = self.middleware.process_request(request)
        ok_(isinstance(response, HttpResponseRedirect))
        eq_(response.url, '/en/version-100t/demo-tips')

    @override_settings(VERSIONS_LOCALE_MAP=TEST_VERSIONS_LOCALE_MAP)
    def test_with_nonexistant_version(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path = '/xx/version-does-not-exist/demo-tips'
        eq_(self.middleware.process_request(request), None)

    def test_with_nonexistant_locale(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path = '/xx/version-100t/demo-tips'
        eq_(self.middleware.process_request(request), None)

    def test_request_path_breakdown_failure(self):
        request = Mock()
        request.user.is_authenticated.return_value = False
        request.path = '/'
        eq_(self.middleware.process_request(request), None)
