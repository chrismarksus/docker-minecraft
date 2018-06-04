
def signFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

def chestFilter(poi):
    if poi['id'] == "Chest":
        return ("Chest", "Chest with %d items" % len(poi['Items']))

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['My World'] = "/world"

# Define where to put the output here.
outputdir = "/www"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

renders["default"] = {
        'world': 'My World',
        'title': 'A regular render',
        'markers': [dict(name="All signs", filterFunction=signFilter),
                    dict(name="Chests", filterFunction=chestFilter, icon="chest.png", createInfoWindow=False)]
}
renders["night"] = {
        'world': 'My World',
        'title': 'A night render',
        'rendermode': 'night',
}
renders["cave"] = {
        'world': 'My World',
        'title': 'A cave render',
        'rendermode': 'cave',
}
# This example is the same as above, but rotated
renders["render2"] = {
        'world': 'My World',
        'northdirection': 'upper-right',
        'title': 'Upper-right north direction',
}
renders["render3"] = {
        'world': 'My World',
        'northdirection': 'lower-right',
        'title': 'Lower-right north direction',
}
renders["render4"] = {
        'world': 'My World',
        'northdirection': 'upper-left',
        'title': 'Upper-left north direction',
}
renders["render4"] = {
        'world': 'My World',
        'northdirection': 'lower-left',
        'title': 'Lower-left north direction',
}
