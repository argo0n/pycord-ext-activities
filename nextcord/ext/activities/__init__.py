from typing import Optional, Union

from nextcord import InviteTarget, Invite, VoiceChannel

from .enums import Activity, ActivityDevelopment

__version__ = "2022.03.15"
__author__ = "MaskDuck"
__license__ = "MIT License"


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
    """|coro|

    Creates an instant invite for the specified activity.

    You must have the :attr:`~nextcord.Permissions.create_instant_invite` permission to
    do this.

    Parameters
    ------------
    activity: Union[:class:`.Activity`, :class:`.ActivityDevelopment`]
        The activity to create an invite link for. ``activity_id`` must be specified if this is :attr:`Activity.custom`.
    activity_id: Optional[:class:`int`]
        The ID of the activity to create an invite link for. This can not be ``None`` if ``activity`` is of type ``Activity.custom``.
    max_age: :class:`int`
        How long the invite should last in seconds. If it's 0 then the invite
        doesn't expire. Defaults to ``0``.
    max_uses: :class:`int`
        How many uses the invite could be used for. If it's 0 then there
        are unlimited uses. Defaults to ``0``.
    temporary: :class:`bool`
        Denotes that the invite grants temporary membership
        (i.e. they get kicked after they disconnect). Defaults to ``False``.
    unique: :class:`bool`
        Indicates if a unique invite URL should be created. Defaults to True.
        If this is set to ``False`` then it will return a previously created
        invite.
    reason: Optional[:class:`str`]
        The reason for creating this invite. Shows up on the audit log.

    Raises
    -------
    ~nextcord.HTTPException
        Invite creation failed.

    Returns
    --------
    :class:`~nextcord.Invite`
        The invite that was created to launch the specified activity.
    """
    if activity is Activity.custom:
        if activity_id is None:
            raise ValueError("activity_id is required for Activity.custom")

        activity_id = int(activity_id)
    else:
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
