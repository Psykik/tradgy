"""
misc. notes;
- twint folder is a clone of my repo (`git clone --depth=1 https://github.com/mechabubba/twint.git`)
    - solely because i was having an issue with it crashing when trying to grab tweets; made a pr and should work without issues now. nothing else has changed.
    - **to install dependencies on windows:** you must install some libraries from visual studio.
        - https://visualstudio.microsoft.com/visual-cpp-build-tools/ 
        - once you're there launch that and click "Desktop development with C++", check first five boxes on the right, install
    - then cd into twint folder and `py -m pip install . -r requirements.txt`
"""

import re
import threading
import time
import twint
from datetime import date, timedelta

# time range for when we scrape tweets
# this will still only pull the 
start = date.today()
end = timedelta(weeks=4)

# configure your search through this object
# see https://github.com/twintproject/twint/wiki/Configuration for all configuration options
c = twint.Config()
c.Near = "Chicago" # required if making a general search w/o username.
#c.Limit = 200 # disabling this will result in an infinite stream of tweets from the start timestamp
#c.Verified = True
c.Since = (start - end).isoformat()
c.Store_csv = True
c.Stats = False
c.Format = ""

def get_tweets(conf):
    conf.Output = "./csv/{}.csv".format(int(time.time() * 1000))
    twint.run.Search(c)

# multithreading is completely unnecessary here
if __name__ == "__main__":
    # very shitty attempt at "faking" real time tweets
    # - start thread to get tweets
    #     - we will ignore how completely unnecessary multithreading is here but whatever
    # - end it after a certain amount of time
    # - restart.
    # 
    # twint only gets geotagged tweets if they're *specifically* geotagged, severely limiting what we can get with it.
    # the twitter api has naturally geotagged tweets... which we dont have access to :,)
    #words = ["ablaze", "accident", "aftershock", "airplane", "ambulance", "annihilated", "annihilation", "apocalypse", "armageddon", "army", "arson", "arsonist", "attack", "attacked", "avalanche", "bag", "bagging", "bags", "bang", "battle", "bioterror", "bioterrorism", "blaze", "blazing", "bleeding", "blew", "blight", "blizzard", "blood", "bloody", "blown", "body", "bomb", "bombed", "bomber", "bombing", "bridge", "buildings", "burned", "burning", "bush", "casualties", "casualty", "catastrophe", "catastrophic", "chemical", "cliff", "collapse", "collapsed", "collide", "collided", "collision", "crash", "crashed", "crush", "crushed", "curfew", "cyclone", "damage", "danger", "dead", "death", "deaths", "debris", "deluge", "deluged", "demolish", "demolished", "demolition", "derail", "derailed", "derailment", "desolate", "desolation", "destroy", "destroyed", "destruction", "detonate", "detonation", "devastated", "devastation", "disaster", "displaced", "drought", "drown", "drowned", "drowning", "dust", "earthquake", "electrocute", "electrocuted", "emergency", "engulfed", "epicentre", "evacuate", "evacuated", "evacuation", "explode", "exploded", "explosion", "eyewitness", "failure", "fall", "famine", "fatal", "fatalities", "fatality", "fear", "fire", "fires", "first", "flames", "flattened", "flood", "flooding", "floods", "forest", "hail", "hailstorm", "harm", "hazard", "hazardous", "heat", "hellfire", "hijack", "hijacker", "hijacking", "hostage", "hostages", "hurricane", "injured", "injuries", "injury", "inundated", "inundation", "landslide", "lava", "lightning", "loud", "mass", "massacre", "mayhem", "meltdown", "military", "mudslide", "murder", "murderer", "natural", "nuclear", "obliterate", "obliterated", "obliteration", "oil", "on", "outbreak", "pandemonium", "panic", "panicking", "plan", "police", "quarantine", "quarantined", "radiation", "rainstorm", "razed", "reactor", "refugees", "rescue", "rescued", "rescuers", "responders", "riot", "rioting", "rubble", "ruin", "sandstorm", "screamed", "screaming", "screams", "seismic", "services", "sinkhole", "sinking", "siren", "sirens", "smoke", "snowstorm", "spill", "storm", "stretcher", "structural", "suicide", "sunk", "survive", "survived", "survivors", "terrorism", "terrorist", "threat", "thunder", "thunderstorm", "tornado", "tragedy", "trapped", "trauma", "traumatised", "trouble", "truck", "tsunami", "twister", "typhoon", "up", "upheaval", "violent", "volcano", "war", "wave", "weapon", "weapons", "whirlwind", "wild", "wildfire", "windstorm", "wounded", "wounds", "wreck", "wreckage", "wrecked", "zone"]
    #good = []

    get_tweets(c)

    #while True:
        #tweets = threading.Thread(target=get_tweets, args=(c,))
        #tweets.start()

        #time.sleep(10)

        #tweets.setIsTerminating(true) # tells thread to stop
        #tweets.join() # wait for the thread to stop

        #print(len(twint.output.tweets_list))
        #print(type(twint.output.tweets_list))
        #print(twint.output.tweets_list[0])

        #for tweetobj in twint.output.tweets_list:
            #if not any(x in tweetobj.tweet for x in words):
                #continue
            #if not tweetobj.place and not tweetobj.geo:
                #continue
            #good.append(tweetobj)
        
        #print(len(good))

        #time.sleep(8)

