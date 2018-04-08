======================
spotify-webplayer-accesstoken
======================

Utility script to get Spotify'92s web player access token which has more permissions than the normal one that can be obtained through the Spotify API.

This was inspired by `kopiro'92s`<https://github.com/kopiro>` work on the same thing on Node (`link<https://github.com/kopiro/node-spotify-webplayer-accesstoken>').

Installing
============
::bash
    pip install spotify_token

Usage
============
An access token can be obtained by running the following:

::python
    from spotify_token import util

    data = util.start_session("myusername","mypassword")
    access_token = data[0]
    expiration_date = data[1]

License
============

This project is licensed under the MIT License - see the `LICENSE<LICENSE>` file for details}