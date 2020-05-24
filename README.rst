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

To obtain the cookies (valid for 1 year):
* Open a new __Incognito window__ in Chrome (or another browser) at https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F
* Open Developer Tools in your browser (might require developer menu to be enabled in some browsers)
* Login to Spotify.
* Search/Filter for `get_access_token` in Developer tools under Network.
* Under cookies for the request save the values for `sp_dc` and `sp_key`.
* Close the window without logging out (Otherwise the cookies are made invalid).

An access token can be obtained by running the following::

    import spotify_token as st

    data = st.start_session("sp_dc","sp_key")
    access_token = data[0]
    expiration_date = data[1]

License
============

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details
