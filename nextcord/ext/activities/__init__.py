from typing import Optional, Union
from .enums import Activity, ActivityDevelopment

from nextcord import InviteTarget, Invite, VoiceChannel


__version__ = "2022.03.15"
__author__ = "MaskDuck"
__license__ = "GNU General Public License Version 3.0"


async def create_activity_invite_link(
    self: VoiceChannel,
    activity: Union[Activity, ActivityDevelopment],
    /,
    *,
    activity_id: Optional[int] = None,
    reason: Optional[str] = None,
    max_age: int = 0,
    max_uses: int = 0,
    temporary: bool = False,
    unique: bool = True,
) -> Invite:
    """
    Creates an invite link for the specified activity.

    Parameters
    -----------
    activity: Union[:class:`.Activity`, :class:`.ActivityDevelopment`]
        The activity to create an invite link for.
        If the value is ``Activity.custom`` and you don't pass the ``activity_id`` parameter, this will lead to an exception.
    activity_id: Optional[:class:`int`]
        The ID of the activity to create an invite link for, if ``activity`` parameter is of type ``Activity.custom`` it's ignored otherwise.

    Returns
    --------
    :class:`nextcord.Invite`
        The invite that was created to launch the specific activity.
    """
    if activity is Activity.custom:
        if activity_id is None:
            raise ValueError("activity_id is required for Activity.custom")

        activity_id = int(activity_id)
    else:
        if activity.is_boost_locked and self.guild.premium_tier < 1:
            raise ValueError(
                "This activtity is boost-locked. Boost-locked activities are only available for guilds with a premium tier of 1 or higher"
            )

        activity_id = int(activity)

    res = await self.create_invite(
        reason=reason,
        max_age=max_age,
        max_uses=max_uses,
        temporary=temporary,
        unique=unique,
        target_type=InviteTarget.embedded_application,
        target_application_id=activity_id,
    )

    return res


VoiceChannel.create_activity_invite = create_activity_invite_link  # type: ignore
