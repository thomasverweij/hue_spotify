# hue_spotify
Set the mood with spotify and philips hue. <br/>
This is just an extremely simple experiment for now. 

## requirements
- spotify account
- [spotify api credentials](https://developer.spotify.com/dashboard/)
- ip address of hue bridge
- python3
- git

## setup
- run the following commands:
```sh
git clone https://github.com/thomasverweij/hue_spotify.git
cd hue_spotify
python3 -m venv .v && source .v/bin/activate && pip install -r requirements.txt
```
- edit credentials in run_app.sh

## run
```sh
sh run_app.sh
```
!! make sure to follow the steps to set up authentication when running this for the first time