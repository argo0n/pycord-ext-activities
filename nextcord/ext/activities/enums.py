from enum import Enum


class ActivityBase(Enum):
    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        if not self.value:
            return 0

        return self.value

    @property
    def is_boost_locked(self) -> bool:
        return False


class Activity(ActivityBase):
    # you can insert activity_id parameter while setting this as activities,
    # honestly very useless since nextcord already have target_application_id, but heck yeah
    custom = None
    poker = 755827207812677713  # boost-locked
    betrayal = 773336526917861400
    fishington = 814288819477020702
    chess = 832012774040141894  # boost-locked
    checker = 832013003968348200  # boost-locked
    youtube = 880218394199220334
    doodle = 878067389634314250
    word_snacks = 879863976006127627
    sketch = 902271654783242291
    spellcast = 852509694341283871  # boost-locked
    letter_league = 879863686565621790  # boost-locked
    awkword = 879863881349087252  # boost-locked
    blazing = 832025144389533716
    putt_party = 945737671223947305

    # aliases for legacy reasons
    letter_tile = letter_league  # boost-locked, now named letter_league
    ocho = blazing  # boost-locked
    watch_together = youtube

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


# https://gist.github.com/GeneralSadaf/42d91a2b6a93a7db7a39208f2d8b53ad#development-versions
class ActivityDevelopment(ActivityBase):
    putt_party = 910224161476083792
    sketch = 879864104980979792
    doodle = 878067427668275241
    youtube = 880218832743055411
    PN = 763133495793942528
    word_snacks = 879864010126786570
    decoder = 891001866073296967
