from datetime import date, datetime, timedelta

import geocoder
import requests
from astral import LocationInfo, today
from astral.sun import sun
from textual.app import ReturnType


class ShabbasTimer:
    def __init__(self) -> None:
        self.geo = geocoder.ip("me")  # And self.geo.ip is IP
        self.site_api = "http://ipwho.is"  # This api site to get timezone

    def get_tz(self, site_api="http://ipwho.is", ip=None):
        response = requests.get(f"{site_api}/{ip}").json()  # Get json from site
        return response["timezone"]["id"]

    def get_geoloc(self):
        lat = float(self.geo.lat)
        lng = float(self.geo.lng)
        city = self.geo.city
        country = self.geo.country
        tz = self.get_tz(ip=self.geo.ip)
        return LocationInfo(
            name=city,
            region=country,
            timezone=tz,
            latitude=lat,
            longitude=lng,
        )

    def get_shabbas(self, today, weekday):
        today_weekday = today.weekday()
        days_until = (weekday - today_weekday) % 7
        return today + timedelta(days=days_until)

    def get_time_until(self, weekday):
        target_date = self.get_shabbas(
            date.today(), weekday
        )  # 4 is friday and 5 is saturday in date.weekday
        suntime = sun(self.get_geoloc().observer, date=target_date)
        shabbas_start_time = suntime["dusk"]
        shabbas = datetime.combine(target_date, shabbas_start_time.time())
        now = datetime.combine(date.today(), datetime.now().time())
        return shabbas - now

    def get_time(self):
        time_until_start = self.get_time_until(4)
        if time_until_start.total_seconds() < 0:
            time_until_end = self.get_time_until(5)

            if time_until_end.total_seconds() < 0:
                return f"Shabbat start in {self.get_time_until(4)}"
            else:
                return f"Shabbat end in {time_until_end}"
        else:
            return f"Shabbat start in {time_until_start}"


# BRB
# I will add here sqlite support
