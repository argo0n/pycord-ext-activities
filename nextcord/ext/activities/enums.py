from enum import Enum


class Activity(Enum):
    # you can insert activity_id parameter while setting this as activities,
    # honestly very useless since nextcord already have target_application_id, but heck yeah
    custom = None
    poker = 755827207812677713  # boost-locked
    betrayal = 773336526917861400
    fishington = 814288819477020702
    chess = 832012774040141894  # boost-locked
    checker = 832013003968348200  # boost-locked
    ocho = 832025144389533716  # boost-locked
    youtube = 880218394199220334
    doodle = 878067389634314250
    letter_tile = 879863686565621790  # boost-locked, now named letter_league
    word_snacks = 879863976006127627
    sketch = 902271654783242291
    spellcast = 852509694341283871  # boost-locked
    letter_league = 879863686565621790  # boost-locked
    awkword = 879863881349087252  # boost-locked
    blazing = 1832025144389533716

    def __int__(self) -> int:
        if not self.value:
            return 0

        return self.value

    @property
    def is_boost_locked(self) -> bool:
        return self in (
            Activity.poker,
            Activity.chess,
            Activity.checker,
            Activity.ocho,
            Activity.letter_tile,
            Activity.spellcast,
            Activity.letter_league,
            Activity.awkword,
        )
