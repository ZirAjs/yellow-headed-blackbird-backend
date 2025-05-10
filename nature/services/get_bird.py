from datetime import time
import random

# 하드코딩된 Bird 리스트
birds = [
    {"name": "Sparrow", "time": time(0), "description": "Quietly roosting for the night."},
    {"name": "Nightingale", "time": time(0), "description": "Silently perched in the darkness."},
    {"name": "Eagle", "time": time(0), "description": "Resting high in its nest under the moonlight."},
    {"name": "Parrot", "time": time(0), "description": "Dreaming of colorful fruits."},
    {"name": "Korean Bush Warbler", "time": time(0), "description": "Huddled down, keeping warm in the night."},
    {"name": "Pale Thrush", "time": time(1), "description": "Starting to stir as the first hints of dawn appear."},
    {"name": "Japanese Green Woodpecker", "time": time(1), "description": "Listening intently for early morning insects."},
    {"name": "Mallard", "time": time(1), "description": "Peacefully floating on the still water."},
    {"name": "Grey Heron", "time": time(1), "description": "Standing still, waiting for an unsuspecting fish."},
    {"name": "Eastern Spot-billed Duck", "time": time(1), "description": "Singing a soft pre-dawn chorus."},
    {"name": "Scops Owl", "time": time(2), "description": "Its nocturnal calls fading as morning approaches."},
    {"name": "Woodpecker", "time": time(2), "description": "Beginning its rhythmic drumming on a tree trunk."},
    {"name": "Hawk", "time": time(2), "description": "Soaring silently, scanning the awakening landscape."},
    {"name": "Crow", "time": time(2), "description": "Cawing loudly, announcing the start of the day."},
    {"name": "Finch", "time": time(2), "description": "Flitting between branches, chirping cheerfully."},
    {"name": "Pigeon", "time": time(3), "description": "Gathering in the city square, looking for breakfast."},
    {"name": "Duck", "time": time(3), "description": "Paddling along the pond, leaving gentle ripples."},
    {"name": "Pelican", "time": time(3), "description": "Stretching its large wings, ready for a morning flight."},
    {"name": "Swallow", "time": time(3), "description": "Dipping and diving, catching early flying insects."},
    {"name": "Stork", "time": time(3), "description": "Majestically wading in the shallows."},
    {"name": "Owl", "time": time(4), "description": "Returning to its roost after a night of hunting."},
    {"name": "Kingfisher", "time": time(4), "description": "Perched patiently, waiting for a flash of silver below."},
    {"name": "Goose", "time": time(4), "description": "Honking loudly as it grazes in the open field."},
    {"name": "Robin", "time": time(4), "description": "Singing its melodious morning song."},
    {"name": "Kite", "time": time(4), "description": "Circling high above, searching for prey."},
    {"name": "Sparrow", "time": time(5), "description": "Busily foraging for seeds and insects."},
    {"name": "Nightingale", "time": time(5), "description": "Singing a complex and beautiful song."},
    {"name": "Eagle", "time": time(5), "description": "Hunting for its morning meal with sharp eyes."},
    {"name": "Parrot", "time": time(5), "description": "Chattering loudly in the canopy."},
    {"name": "Korean Bush Warbler", "time": time(5), "description": "Darting through the undergrowth."},
    {"name": "Pale Thrush", "time": time(6), "description": "Enjoying the warmth of the rising sun."},
    {"name": "Japanese Green Woodpecker", "time": time(6), "description": "Continuing its search for insects on tree bark."},
    {"name": "Mallard", "time": time(6), "description": "Swimming actively, perhaps looking for food."},
    {"name": "Grey Heron", "time": time(6), "description": "Taking flight with slow, deliberate wing beats."},
    {"name": "Eastern Spot-billed Duck", "time": time(6), "description": "Building or tending to its nest."},
    {"name": "Scops Owl", "time": time(7), "description": "Sleeping soundly in a shaded spot."},
    {"name": "Woodpecker", "time": time(7), "description": "Excavating a hole, possibly for a nest."},
    {"name": "Hawk", "time": time(7), "description": "Perched on a high branch, observing its territory."},
    {"name": "Crow", "time": time(7), "description": "Investigating something shiny on the ground."},
    {"name": "Finch", "time": time(7), "description": "Feeding on seeds in a sunny patch."},
    {"name": "Pigeon", "time": time(8), "description": "Strutting confidently along a rooftop."},
    {"name": "Duck", "time": time(8), "description": "Dabbling in the water, tail up."},
    {"name": "Pelican", "time": time(8), "description": "Gliding gracefully over the water's surface."},
    {"name": "Swallow", "time": time(8), "description": "Soaring high in the sky, catching insects on the wing."},
    {"name": "Stork", "time": time(8), "description": "Flying slowly over the wetlands."},
    {"name": "Owl", "time": time(9), "description": "Hidden away, sleeping during the day."},
    {"name": "Kingfisher", "time": time(9), "description": "Darting out from its perch and plunging into the water."},
    {"name": "Goose", "time": time(9), "description": "Leading its goslings across the grass."},
    {"name": "Robin", "time": time(9), "description": "Pulling a worm from the soil."},
    {"name": "Kite", "time": time(9), "description": "Hovering momentarily before swooping down."},
    {"name": "Sparrow", "time": time(10), "description": "Chirping amongst the leaves in a tree."},
    {"name": "Nightingale", "time": time(10), "description": "Singing loudly from a high vantage point."},
    {"name": "Eagle", "time": time(10), "description": "Carrying prey back to its nest."},
    {"name": "Parrot", "time": time(10), "description": "Mimicking sounds it hears in the environment."},
    {"name": "Korean Bush Warbler", "time": time(10), "description": "Searching for food in a dense bush."},
]

def get_daily_bird(input_time: time):
    minutes = input_time.minute
    if minutes < 30:
        target_time = time(input_time.hour, 0)
    else:
        target_time = time((input_time.hour + 1)%24, 0)

    active_birds = [bird for bird in birds if bird["time"] == target_time]
    
    # 해당 시간대에 맞는 bird 중 랜덤으로 하나 선택
    if active_birds:
        return random.choice(active_birds)
    else:
        return birds[0]