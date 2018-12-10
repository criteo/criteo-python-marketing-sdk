from __future__ import absolute_import

import unittest

import pook

import criteo_marketing
from criteo_marketing import Configuration
from criteo_marketing.rest import ApiException


class TestClientRefreshToken(unittest.TestCase):

    def setUp(self):
        self.configuration = Configuration()
        self.configuration.host = "https://example.com/api"
        self.configuration.username = "my_client_id"
        self.configuration.password = "my_password"
        self.client = criteo_marketing.ApiClient(self.configuration)

        pook.reset()

    @pook.on
    def testDoesNotInterceptRequestWhenNoAuthorizationHeader(self):
        (pook.get('https://example.com/api/v1/valid/url')
         .times(1)
         .reply(200)
         .type('json')
         .json({'status': 'ok'}))

        header_params_without_authorization = {'Accept': 'application/json'}
        res = self.a_get_request(header_params_without_authorization)

        self.assertTrue(pook.isdone())
        self.assertEqual(res, {'status': 'ok'})

    @pook.on
    def testAlwaysSendValidBearerToken(self):
        expired_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdHg6dXNlcjp1bXNJZCI6IjIyNjQyMSIsImN0eDp1c2VyOnVp"
        fresh_token = "kltTjBlKHAxYzJWIiwiY3"

        (pook.post(self.configuration.host + '/oauth2/token')
         .header("Content-Type", "application/x-www-form-urlencoded")
         .body('client_id=%s&client_secret=%s&grant_type=client_credentials' % (self.configuration.username, self.configuration.password))
         .times(1)
         .reply(200)
         .type('json')
         .json(dict(access_token=fresh_token, expires_in=299, token_type="bearer")))

        (pook.get(self.configuration.host + '/v1/valid/url')
         .header('Authorization', "Bearer " + fresh_token)
         .times(1)
         .reply(200)
         .type('json')
         .json({'status': 'ok'}))

        res = self.get_with_expired_token(expired_token)

        self.assertTrue(pook.isdone())
        self.assertEqual(res, {'status': 'ok'})

    @pook.on
    def testShouldThrowErrorWhenCannotRefreshToken(self):
        expired_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC"

        (pook.post(self.configuration.host + '/oauth2/token')
         .times(1)
         .reply(500)
         .type('json')
         .json({'Error': "Unknown Error"}))

        (pook.get(self.configuration.host + '/v1/valid/url')
         .header('Authorization', "Bearer " + expired_token)
         .times(0)
         .reply(200)
         .type('json')
         .json({'message': "can't make this call since client could not refresh expired token"}))

        with self.assertRaises(ApiException) as cm:
            self.get_with_expired_token(expired_token)

        self.assertEqual(cm.exception.status, 500)
        self.assertIn("Cannot refresh token by calling", cm.exception.body["token_error"])
        self.assertTrue(pook.isdone())

    def get_with_expired_token(self, expired_token):
        header_params = {'Accept': 'application/json', 'Authorization': 'Bearer ' + expired_token}
        res = self.a_get_request(header_params)
        return res

    def a_get_request(self, header):
        res = self.client.call_api(
            '/v1/valid/url', 'GET',
            {},
            [],
            header,
            body=None,
            post_params=[],
            files={},
            response_type='object',
            auth_settings=[],
            async_req=None,
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={})
        return res


if __name__ == '__main__':
    unittest.main()
