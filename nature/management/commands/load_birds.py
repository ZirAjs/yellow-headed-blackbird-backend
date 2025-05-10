from django.core.management.base import BaseCommand
from nature.models import Bird
from datetime import time

class Command(BaseCommand):
    help = 'Load hardcoded bird data'

    def handle(self, *args, **kwargs):
        # 기존 데이터 삭제
        Bird.objects.all().delete()

        # 넣게 될 새(Bird) 데이터
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
            {"name": "Blue Jay", "time": time(11), "description": "Boldly searching for acorns in the bright daylight."},
            {"name": "Cardinal", "time": time(11), "description": "A flash of vibrant red against the green leaves."},
            {"name": "Hummingbird", "time": time(11), "description": "Darting from flower to flower, sipping nectar."},
            {"name": "Mockingbird", "time": time(11), "description": "Imitating the calls of other birds in its repertoire."},
            {"name": "Dove", "time": time(11), "description": "Peacefully cooing on a telephone wire."},
            # Hour 12 (Midday)
            {"name": "Osprey", "time": time(12), "description": "Circling high above the water, ready to plunge for fish."},
            {"name": "Lark", "time": time(12), "description": "Singing its soaring melody high in the sky."},
            {"name": "Swift", "time": time(12), "description": "Flying at incredible speed, catching insects mid-air."},
            {"name": "Buzzard", "time": time(12), "description": "Soaring lazily on thermal currents."},
            {"name": "Quail", "time": time(12), "description": "Hiding in the tall grass, making soft calls."},
            # Hour 13 (1 PM)
            {"name": "Heron", "time": time(13), "description": "Stalking patiently at the water's edge."},
            {"name": "Kingfisher", "time": time(13), "description": "Sitting still on a branch overhanging the stream."},
            {"name": "Jay", "time": time(13), "description": "Scolding loudly from the treetops."},
            {"name": "Starling", "time": time(13), "description": "Gathering in large, chattering flocks."},
            {"name": "Wren", "time": time(13), "description": "Foraging busily in a tangled bush."},
            # Hour 14 (2 PM)
            {"name": "Egret", "time": time(14), "description": "Gracefully wading through shallow water."},
            {"name": "Sandpiper", "time": time(14), "description": "Running along the beach, probing the sand."},
            {"name": "Thrush", "time": time(14), "description": "Singing a rich, flute-like song from a hidden perch."},
            {"name": "Goldfinch", "time": time(14), "description": "Feeding on thistle seeds, flashing its yellow wings."},
            {"name": "Phoebe", "time": time(14), "description": "Perched on a low branch, twitching its tail."},
            # Hour 15 (3 PM)
            {"name": "Kestrel", "time": time(15), "description": "Hovering in the wind, searching for small mammals."},
            {"name": "Nuthatch", "time": time(15), "description": "Creeping headfirst down a tree trunk."},
            {"name": "Chickadee", "time": time(15), "description": "Hanging upside down to reach a tasty seed."},
            {"name": "Towhee", "time": time(15), "description": "Scratching vigorously in the leaf litter."},
            {"name": "Grackle", "time": time(15), "description": "Striding across the lawn with a glossy sheen."},
            # Hour 16 (4 PM)
            {"name": "Shrike", "time": time(16), "description": "Perched watchfully on a thorny bush."},
            {"name": "Teal", "time": time(16), "description": "Dipping its head underwater in a shallow pond."},
            {"name": "Cormorant", "time": time(16), "description": "Standing on a rock, wings spread to dry."},
            {"name": "Magpie", "time": time(16), "description": "Flitting about, collecting twigs for its nest."},
            {"name": "Junco", "time": time(16), "description": "Pecking at the ground for fallen seeds."},
            # Hour 17 (5 PM)
            {"name": "Woodcock", "time": time(17), "description": "Beginning its twilight sky dance."},
            {"name": "Whippoorwill", "time": time(17), "description": "Starting to call as dusk approaches."},
            {"name": "Brown Thrasher", "time": time(17), "description": "Rummaging through leaves with its long bill."},
            {"name": "Belted Kingfisher", "time": time(17), "description": "Giving its rattling call as it flies by."},
            {"name": "Common Redpoll", "time": time(17), "description": "Clinging to catkin branches, feeding on seeds."},
            # Hour 18 (6 PM)
            {"name": "Barn Swallow", "time": time(18), "description": "Flying low over fields as evening falls."},
            {"name": "American Bittern", "time": time(18), "description": "Standing motionless amongst the reeds."},
            {"name": "Common Nighthawk", "time": time(18), "description": "Hawking for insects in the twilight sky."},
            {"name": "Hermit Thrush", "time": time(18), "description": "Singing its ethereal evening song."},
            {"name": "Evening Grosbeak", "time": time(18), "description": "Gathering at feeders as the day ends."},
            # Hour 19 (7 PM)
            {"name": "Great Horned Owl", "time": time(19), "description": "Hooting softly as darkness descends."},
            {"name": "Common Poorwill", "time": time(19), "description": "Beginning its repeated calls in the dim light."},
            {"name": "Blackbird", "time": time(19), "description": "Singing its last melodious notes of the day."},
            {"name": "Chipping Sparrow", "time": time(19), "description": "Giving its trilling call before settling down."},
            {"name": "Cedar Waxwing", "time": time(19), "description": "Perched closely together on a branch."},
            # Hour 20 (8 PM)
            {"name": "Screech Owl", "time": time(20), "description": "Giving its eerie, wavering call in the night."},
            {"name": "Nightjar", "time": time(20), "description": "Fluttering silently through the night air."},
            {"name": "Mourning Dove", "time": time(20), "description": "Giving its soft, mournful coo in the quiet evening."},
            {"name": "Song Sparrow", "time": time(20), "description": "Singing softly in the moonlight."},
            {"name": "Northern Flicker", "time": time(20), "description": "Quietly roosting in a tree cavity."},
            # Hour 21 (9 PM)
            {"name": "Barred Owl", "time": time(21), "description": "Calling out with its distinctive 'Who cooks for you?' hoot."},
            {"name": "Long-eared Owl", "time": time(21), "description": "Silently hunting for small rodents."},
            {"name": "Eastern Phoebe", "time": time(21), "description": "Perched still and quiet in the darkness."},
            {"name": "White-throated Sparrow", "time": time(21), "description": "Giving soft chips in its sleep."},
            {"name": "Downy Woodpecker", "time": time(21), "description": "Tucked away in its roosting spot."},
            # Hour 22 (10 PM)
            {"name": "Saw-whet Owl", "time": time(22), "description": "Giving its high-pitched, tooting call."},
            {"name": "Barn Owl", "time": time(22), "description": "Flying silently over fields in search of prey."},
            {"name": "Great Blue Heron", "time": time(22), "description": "Standing still in the shallows under the night sky."},
            {"name": "American Robin", "time": time(22), "description": "Quietly resting on a branch."},
            {"name": "Hairy Woodpecker", "time": time(22), "description": "Asleep in a tree crevice."},
            # Hour 23 (11 PM)
            {"name": "Snowy Owl", "time": time(23), "description": "Its white plumage visible in the moonlight."},
            {"name": "Short-eared Owl", "time": time(23), "description": "Flying low over open country at night."},
            {"name": "Killdeer", "time": time(23), "description": "Giving its piercing 'kill-deer' call in the darkness."},
            {"name": "Carolina Wren", "time": time(23), "description": "Snuggled into a sheltered spot for the night."},
            {"name": "Pileated Woodpecker", "time": time(23), "description": "Resting quietly in its roosting hole."},
        ]
        
        # 새(Bird) 데이터 삽입
        for book in birds:
            Bird.objects.create(**book)
        self.stdout.write(self.style.SUCCESS('New birds data loaded.'))