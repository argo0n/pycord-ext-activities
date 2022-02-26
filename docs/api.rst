API Reference
==============

activities.__version__ 
=======================
Return the version of the wrapper.

nextcord.VoiceChannel.create_activity_invite(activity, activity_id=None)
=========================================================================
Creates an invite link for the specified activity.

Parameters
-----------
activity
    The activity to create an invite link for.
    If the value is ``Activity.custom`` and you don't pass the ``activity_id`` parameter, this will lead to an exception.
    If you want to know which activity is supported, see `supported activities page <https://nextcord-ext-activities.readthedocs.io/en/latest/supported_activities.html>`_.
activity_id
    The ID of the activity to create an invite link for, if ``activity`` parameter is ``Activity.custom``.
    If ``activity`` is not ``Activity.custom``, this parameter is ignored.

Returns
--------
    The invite link to launch the specific activity.

Return type
------------
    ``str``
