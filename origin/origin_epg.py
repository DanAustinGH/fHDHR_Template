import datetime


class OriginEPG():

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def update_epg(self, fhdhr_channels):
        programguide = {}

        todaydate = datetime.datetime.utcnow().date()
        self.remove_stale_cache(todaydate)

        for fhdhr_id in list(fhdhr_channels.list.keys()):
            chan_obj = fhdhr_channels.list[fhdhr_id]

            if str(chan_obj.dict["number"]) not in list(programguide.keys()):
                programguide[str(chan_obj.dict["number"])] = chan_obj.epgdict

        return programguide
