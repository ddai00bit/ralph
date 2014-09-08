# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.core.cache import cache
from django.test import TestCase

from ralph.account.models import BoundPerm, Profile, Perm
from ralph.business.models import Venture
from ralph.discovery.models import (
    ComponentModel,
    ComponentType,
    DeprecationKind,
    DeviceType,
    SplunkUsage,
)
from ralph.ui.tests.util import create_device
from ralph.ui.tests.global_utils import create_user
from tastypie.test import ResourceTestCase


class AccessToDiscoveyApiTest(TestCase):

    def setUp(self):
        self.user = create_user(
            'api_user',
            'test@mail.local',
            'password',
            is_staff=False,
            is_superuser=False,
        )
        self.api_login = {
            'format': 'json',
            'username': self.user.username,
            'api_key': self.user.api_key.key,
        }
        cache.delete("api_user_accesses")

    def get_response(self, resource):
        path = "/api/v0.9/%s/" % resource
        response = self.client.get(
            path=path,
            data=self.api_login,
            format='json',
        )
        return response

    def add_perms(self, perms):
        user_profile = Profile.objects.get(user=self.user)
        for perm in perms:
            BoundPerm(profile=user_profile, perm=perm).save()

    def test_ipaddress_resource(self):
        resource = 'ipaddress'
        perms = [Perm.read_network_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)


    def test_model_resource(self):
        resource = 'model'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)

    def test_device_resource(self):
        resource = 'dev'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)

    def test_physicalserver_resource(self):
        resource = 'physicalserver'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)

    def test_rackserver_resource(self):
        resource = 'rackserver'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)

    def test_bladeserver_resource(self):
        resource = 'bladeserver'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)

    def test_virtualserver_resource(self):
        resource = 'virtualserver'
        perms = [Perm.read_dc_structure, ]

        schema = '%s/schema' % resource
        response = self.get_response(schema)
        self.assertEqual(response.status_code, 200)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 401)

        # Add perms to display resources
        self.add_perms(perms=perms)

        response = self.get_response(resource)
        self.assertEqual(response.status_code, 200)
