"""
using the og twitter api here

these are my creds feel free to use them lol

this **will not work** until we gain elevated access to the twitter api.
"""

from dotenv import load_dotenv
import twitter
load_dotenv()

APIKEY = os.getenv("APIKEY")
APISECRET = os.getenv("APISECRET")
ACCESSTOKEN = os.getenv("ACCESSTOKEN")
ACCESSSECRET = os.getenv("ACCESSSECRET")
BEARERTOKEN = os.getenv("BEARERTOKEN")

words = ["ablaze", "accident", "aftershock", "airplane", "ambulance", "annihilated", "annihilation", "apocalypse", "armageddon", "army", "arson", "arsonist", "attack", "attacked", "avalanche", "bag", "bagging", "bags", "bang", "battle", "bioterror", "bioterrorism", "blaze", "blazing", "bleeding", "blew", "blight", "blizzard", "blood", "bloody", "blown", "body", "bomb", "bombed", "bomber", "bombing", "bridge", "buildings", "burned", "burning", "bush", "casualties", "casualty", "catastrophe", "catastrophic", "chemical", "cliff", "collapse", "collapsed", "collide", "collided", "collision", "crash", "crashed", "crush", "crushed", "curfew", "cyclone", "damage", "danger", "dead", "death", "deaths", "debris", "deluge", "deluged", "demolish", "demolished", "demolition", "derail", "derailed", "derailment", "desolate", "desolation", "destroy", "destroyed", "destruction", "detonate", "detonation", "devastated", "devastation", "disaster", "displaced", "drought", "drown", "drowned", "drowning", "dust", "earthquake", "electrocute", "electrocuted", "emergency", "engulfed", "epicentre", "evacuate", "evacuated", "evacuation", "explode", "exploded", "explosion", "eyewitness", "failure", "fall", "famine", "fatal", "fatalities", "fatality", "fear", "fire", "fires", "first", "flames", "flattened", "flood", "flooding", "floods", "forest", "hail", "hailstorm", "harm", "hazard", "hazardous", "heat", "hellfire", "hijack", "hijacker", "hijacking", "hostage", "hostages", "hurricane", "injured", "injuries", "injury", "inundated", "inundation", "landslide", "lava", "lightning", "loud", "mass", "massacre", "mayhem", "meltdown", "military", "mudslide", "murder", "murderer", "natural", "nuclear", "obliterate", "obliterated", "obliteration", "oil", "on", "outbreak", "pandemonium", "panic", "panicking", "plan", "police", "quarantine", "quarantined", "radiation", "rainstorm", "razed", "reactor", "refugees", "rescue", "rescued", "rescuers", "responders", "riot", "rioting", "rubble", "ruin", "sandstorm", "screamed", "screaming", "screams", "seismic", "services", "sinkhole", "sinking", "siren", "sirens", "smoke", "snowstorm", "spill", "storm", "stretcher", "structural", "suicide", "sunk", "survive", "survived", "survivors", "terrorism", "terrorist", "threat", "thunder", "thunderstorm", "tornado", "tragedy", "trapped", "trauma", "traumatised", "trouble", "truck", "tsunami", "twister", "typhoon", "up", "upheaval", "violent", "volcano", "war", "wave", "weapon", "weapons", "whirlwind", "wild", "wildfire", "windstorm", "wounded", "wounds", "wreck", "wreckage", "wrecked", "zone"]

api = twitter.Api(
    consumer_key=APIKEY,
    consumer_secret=APISECRET,
    access_token_key=ACCESSTOKEN,
    access_token_secret=ACCESSSECRET
)

tweetz = api.GetSearch(
    raw_query=" OR ".join(words), # supporting twitters natural search querying.
    geocode=["41.8781", "87.6298", "1mi"]
)

print(tweet)