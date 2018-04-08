==============================
spotify-webplayer-accesstoken
==============================

Utility script to get Spotify's web player access token which has more permissions than the normal one that can be obtained through the Spotify API.

This was inspired by `kopiro <https://github.com/kopiro>`_'s work on the same thing on Node (`link <https://github.com/kopiro/node-spotify-webplayer-accesstoken>`_).

Installing
============ 

::

    pip install spotify_token

Usage
============
An access token can be obtained by running the following::

    import spotify_token as st

    data = st.start_session("myusername","mypassword")
    access_token = data[0]
    expiration_date = data[1]

License
============

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details
