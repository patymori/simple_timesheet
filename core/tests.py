from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch

from core.views import home_page
from core.models import TimeSheetPediod


datetime_test = datetime(2017, 4, 8, 17, 35, 23)


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        time_now = datetime.now().strftime('%H:%M')
        response = self.client.post('/')
        self.assertIn(time_now, response.content.decode())


class TimeSheetPediodModelTest(TestCase):

    @patch.object(TimeSheetPediod._meta.get_field('start_time'),
                  'default',
                  new=lambda: datetime_test)
    def test_saving_punch_in(self):
        time_sheet_period = TimeSheetPediod()
        time_sheet_period.save()

        saved_periods = TimeSheetPediod.objects.all()
        self.assertEqual(saved_periods.count(), 1)
        self.assertEqual(time_sheet_period.start_time, datetime_test)
