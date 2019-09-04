# hue_spotify
Set the mood with spotify and philips hue. <br/>
This is just an extremely simple experiment for now. 

## requirements
- spotify account
- [spotify api credentials](https://developer.spotify.com/dashboard/)
- ip address of hue bridge
- python3

## setup
run the following commands (fill in your secrets/id/ip):
```bash
git clone https://github.com/thomasverweij/hue_spotify.git
cd hue_spotify
python3 -m venv .v && source .v/bin/activate && pip install -r requirements.txt
export SPOTIFY_CLIENT_ID='<client id>'
export SPOTIFY_SECRET='<client secret>'
export SPOTIFY_USERNAME='<spotify user id>'
export HUE_IP='<hue bridge ip>'

```
## run:
after setup, run:
```bash
python -m hue_spotify
```
you will be prompted to authenticate hue and spotify. after that open [http://127.0.0.1:8080/](http://127.0.0.1:8080/) for the app
