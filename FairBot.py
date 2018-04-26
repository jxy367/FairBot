import discord
import random

TOKEN = 'NDM5MDk1NDg0ODQyMzc3MjE3.DcOLFA.n4Py9tPAmOnFe8fOE6aiGdNyJBo'

client = discord.Client()

# Fair Embeds #
embeds = []
urls = ['http://www.pensacolafair.com/wp-content/themes/wp-responsive110/scripts/timthumb.php?src=http://www.pensacolafair.com/wp-content/uploads/2012/11/midway-night-600x400.jpg&w=600&h=400&zc=1',
        'https://myareanetwork-photos.s3.amazonaws.com/editorphotos/f/26657_1520825140.png',
        'https://media1.fdncms.com/clevescene/imager/u/original/9012469/ohio_state_fair_-_readingandlearning_instagram.png',
        'https://media.nbcwashington.com/images/652*367/fairgrounds071017.jpg',
        'https://d3m7xw68ay40x8.cloudfront.net/assets/2016/10/14163048/1016-state-fair.jpg',
        'http://www.stratfordagriculturalsociety.com/wp-content/uploads/2015/09/FB-Fair-pic.jpg',
        'https://scontent.fbkl1-1.fna.fbcdn.net/v/t31.0-8/11148833_10153519083058322_8334046223350439297_o.jpg?_nc_cat=0&oh=7c835a3f739107548538ca894c06a507&oe=5B9A73E2',
        'https://upload.wikimedia.org/wikipedia/commons/b/b7/L.A._County_Fair_1262.jpg',
        'https://www.gannett-cdn.com/-mm-/c0059ff26d6046b65292170ffc20f75e93874fea/c=0-261-3396-2180&r=x1683&c=3200x1680/local/-/media/2016/10/17/Phoenix/Phoenix/636122964086278930-Arizona-State-Fair-20.jpg',
        'http://www.effinghamcountyfair.com/wp-content/uploads/2014/12/county-fair.jpg',
        'https://i.ytimg.com/vi/2yVeQRcOTi4/maxresdefault.jpg',
        'http://www.lancasterfair.com/wp-content/uploads/2017/01/44.jpg']

for url in urls:
    new_embed = discord.Embed()
    new_embed.set_image(url=url)
    embeds.append(new_embed)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    exact_fair = exactly_in("fair", message.content.lower())
    if exact_fair:
        index = random.randrange(0, len(urls))
        await client.send_message(destination=message.channel, embed=embeds[index])


def exactly_in(str1: str, str2: str):  # str1 exactly in str2
    index = str2.find(str1)
    len_str1 = len(str1)

    if index < 0:
        return False

    if index + len_str1 < len(str2):
        next_char = str2[index + len_str1]
        if next_char.isalpha():
            return False

    if index > 0:
        past_char = str2[index - 1]
        if past_char.isalpha():
            return False

    return True


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
