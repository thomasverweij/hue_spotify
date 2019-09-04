from flask import Flask, render_template, redirect
import phue
from phue import Bridge
import spotipy
import spotipy.util as util
import os
import sys

hue_ip = os.getenv('HUE_IP')
username = os.getenv('SPOTIFY_USERNAME')
client_id=os.getenv('SPOTIFY_CLIENT_ID')
client_secret=os.getenv('SPOTIFY_SECRET')
redirect_uri='http://localhost/'
scope = 'user-modify-playback-state user-read-playback-state'
group = ':)'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<scene>/<track>')
def set_scene_and_song(scene, track):
    sp = spotify_client()
    device = list(filter(lambda x: x['is_active'], [device for device in sp.devices()['devices']]))[0]['id']
    if sp and hb:
        hb.run_scene(group_name=group, scene_name=scene)
        sp.start_playback(device_id=device, uris=['spotify:track:{}'.format(track)])
    else:
        print(sp, hb)
    
    return redirect('/')

def spotify_client():
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
        )
    sp = spotipy.Spotify(auth=token)
    return sp or False

def hue_bridge(ip):
    bridge = Bridge(ip)
    try:
        bridge.connect()
        return bridge
    except:
        print('hue bridge connection error')
        return false

try:
    hb = hue_bridge(hue_ip)
except phue.PhueRegistrationException:
    print('Press button of bridge within 30 seconds and run again')
    sys.exit()
sp = spotify_client()
