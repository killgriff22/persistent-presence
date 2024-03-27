from modules import *

class Custom_Activities:
    class listening(discord.BaseActivity):
        def __init__(self, **kwargs: any) -> None:
            super().__init__(**kwargs)
            self.name = kwargs.get('name', '')
            self.kwargs = kwargs.copy()
            try:
                timestamps: discord.ActivityTimestamps = kwargs['timestamps']
            except KeyError:
                self._start = 0
                self._end = 0
            else:
                self._start = timestamps.get('start', 0)
                self._end = timestamps.get('end', 0)

        @property
        def type(self) -> discord.ActivityType:
            return discord.ActivityType.listening

        def __str__(self) -> str:
            return str(self.name)

        def __repr__(self) -> str:
            return f'<Listening name={self.name!r}>'

        def to_dict(self) -> discord.Activity:
            timestamps: dict[str, any] = {}
            if self._start:
                timestamps['start'] = self._start

            if self._end:
                timestamps['end'] = self._end

            return {
                'type': discord.ActivityType.listening.value,
                'name': str(self.name),
                'timestamps': timestamps,  # type: ignore
                'assets': self.kwargs.get('assets', {}),
                'details': self.kwargs.get('details', ''),
            }

    class playing(discord.BaseActivity):
        def __init__(self, **kwargs: any) -> None:
            super().__init__(**kwargs)
            self.name = kwargs.get('name', '')
            self.kwargs = kwargs.copy()
            try:
                timestamps: discord.ActivityTimestamps = kwargs['timestamps']
            except KeyError:
                self._start = 0
                self._end = 0
            else:
                self._start = timestamps.get('start', 0)
                self._end = timestamps.get('end', 0)  
      
        @property
        def type(self) -> discord.ActivityType:
            return discord.ActivityType.playing

        def __str__(self) -> str:
            return str(self.name)

        def __repr__(self) -> str:
            return f'<Playing name={self.name!r}>'

        def to_dict(self) -> discord.Activity:
            timestamps: dict[str, any] = {}
            if self._start:
                timestamps['start'] = self._start

            if self._end:
                timestamps['end'] = self._end

            return {
                'type': discord.ActivityType.playing.value,
                'name': str(self.name),
                'timestamps': timestamps,  # type: ignore
                'assets': self.kwargs.get('assets', {}),
                'details': self.kwargs.get('details', ''),
            }

    class streaming(discord.BaseActivity):
        def __init__(self, **kwargs: any) -> None:
            super().__init__(**kwargs)
            self.name = kwargs.get('name', '')
            self.kwargs = kwargs.copy()
            self.url = kwargs.get('url', '')
            try:
                timestamps: discord.ActivityTimestamps = kwargs['timestamps']
            except KeyError:
                self._start = 0
                self._end = 0
            else:
                self._start = timestamps.get('start', 0)
                self._end = timestamps.get('end', 0)  
      
        @property
        def type(self) -> discord.ActivityType:
            return discord.ActivityType.streaming

        def __str__(self) -> str:
            return str(self.name)

        def __repr__(self) -> str:
            return f'<Streaming name={self.name!r}>'

        def to_dict(self) -> discord.Activity:
            timestamps: dict[str, any] = {}
            if self._start:
                timestamps['start'] = self._start

            if self._end:
                timestamps['end'] = self._end

            return {
                'type': discord.ActivityType.streaming.value,
                'name': str(self.name),
                'timestamps': timestamps,  # type: ignore
                'assets': self.kwargs.get('assets', {}),
                'details': self.kwargs.get('details', ''),
                'url': self.url,
            }

    class watching(discord.BaseActivity):
        def __init__(self, **kwargs: any) -> None:
            super().__init__(**kwargs)
            self.name = kwargs.get('name', '')
            self.kwargs = kwargs.copy()
            try:
                timestamps: discord.ActivityTimestamps = kwargs['timestamps']
            except KeyError:
                self._start = 0
                self._end = 0
            else:
                self._start = timestamps.get('start', 0)
                self._end = timestamps.get('end', 0)  
      
        @property
        def type(self) -> discord.ActivityType:
            return discord.ActivityType.watching

        def __str__(self) -> str:
            return str(self.name)

        def __repr__(self) -> str:
            return f'<Watching name={self.name!r}>'

        def to_dict(self) -> discord.Activity:
            timestamps: dict[str, any] = {}
            if self._start:
                timestamps['start'] = self._start

            if self._end:
                timestamps['end'] = self._end

            return {
                'type': discord.ActivityType.watching.value,
                'name': str(self.name),
                'timestamps': timestamps,  # type: ignore
                'assets': self.kwargs.get('assets', {}),
                'details': self.kwargs.get('details', ''),
            }