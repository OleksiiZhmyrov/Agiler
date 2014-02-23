from rest_framework import status
from rest_framework.test import APITestCase
from core.models import *
from json import loads, dumps

DEFAULT_TEAM = {'pk': 1, 'name': 'InitTestTeam', 'label': '', 'boards': []}
CORE_URL = '/api/ws100/core'


class TeamTests(APITestCase):

    def setUp(self):
        self.initial_team = Team(name=DEFAULT_TEAM['name'], label=DEFAULT_TEAM['label'])
        self.initial_team.save()

    def test_will_return_response_with_list_of_teams(self):
        response = self.client.get(CORE_URL + '/teams/')
        teams = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(teams), 1)

    def test_team_in_response_has_attributes(self):
        response = self.client.get(CORE_URL + '/teams/')
        teams = response.data['results']
        self.assertEqual(teams, [DEFAULT_TEAM])
