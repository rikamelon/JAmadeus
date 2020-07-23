from src.RedditBot import RedditBot
import json
from datetime import datetime, timedelta
from src import nHentai, UrlHandler, EmbedFactory
import rule34
import random
from jikanpy import Jikan
import wikipedia

with open('data/config.json') as json_data_file:
    data = json.load(json_data_file)

IMAGES_BASE_PATH = "data/forgotten_images"
QUOTES_PATH = "data/quotes.txt"

FORGOTTEN_IMAGES = {

    "test": IMAGES_BASE_PATH + "test.jpg"

}

NON_NSFW_WARNING = "i ain't sending something nsfw in a non nsfw channel"

HELP_MESSAGE = """
---===--- amadeus documentation ---===---

[arg] denotes a required argument
<arg> denotes an optional argument

--------- commands ---------

`/stack`
toggles whether substitutions stack
ex: `/stack`

`/p [subreddit] <sort_method> <number>`
gets the number'th post from subreddit with specified sort_method
default number is 1 and default sort_method is hot
limit of number is 999
ex: `/p eyebleach 2`

`/pm [subreddit] <sort_method> <number>`
gets all posts between 1 and number from subreddit with specified sort_method
default sort_method is hot
limit of number is 9
ex: `/pm eyebleach 9`

`/help`
sends this command
ex: `/help`

`/ping`
get's an ~~incorrect~~ ping
ex: `/ping`

`/f [name]`
pulls a forgotten image, or lists forgotten images if `/f list`
feel free to ping the present phone microwave if you want to add one
ex: `/f test`

`/search [anime]`
searches for an anime on MAL
ex: `/search konosuba`

`/anime [anime]`
gets the specified anime from mal
ex: `/anime konosuba`

`/addquote <quote>`
adds either the last message as a quote or the specified quote
ex: `/quote "bruh" - @iamawesome99#1435`

`/quote <number>`
pulls a quote from a list
if number is unspecified then it pulls a random quote
ex: `/quote 1`

`/quotes`
gets all quotes from the list
ex: `/quotes`

------- NSFW commands ---------

`/r`
get's a random hentai from nhentai
ex: `/r`

`/s [search query]`
searches nhentai for specified search query
ex: `/s shotacon`

`/34 [tag]`
pulls a random result for specified tag from rule34.xxx
ex: `/34 lucina`

`<number>`
will attempt to pull the relevant nhentai if just a number is present in a message
ex: `177013`"""

r_bot = None
r34_bot = None

jikan = Jikan()


async def general(message, bot):

    content = message.content

    if message.channel.id in data['blacklist']['channels']:
        return

    for substitution in bot.substitutions:

        content = substitution(content)

        if not bot.stack and content != message.content:
            break

    if content != message.content:

        await bot.send(content, message.channel)


async def get_post(message, bot, multi=False):
    command = message.content.split(" ")

    try:
        r_bot.authorize()
        if len(command) == 2:
            posts = r_bot.get_posts(command[1], "hot", 1)

        elif len(command) == 3:
            try:
                if int(command[2]) > 1000:
                    await bot.send("bruh that's way too many", message.channel)
                    return
                posts = r_bot.get_posts(command[1], "hot", int(command[2]))
            except ValueError:
                posts = r_bot.get_posts(command[1], command[2], 1)

        elif len(command) == 4:
            if int(command[2]) > 1000:
                await bot.send("bruh that's way too many", message.channel)
                return
            posts = r_bot.get_posts(command[1], command[2], int(command[3]))

        else:
            await bot.send("too many/too little arguments", message.channel)
            return

    except KeyError:
        await bot.send("reddit api error; one of the arguments is wrong", message.channel)
        return

    if not posts:
        await bot.send("no posts found", message.channel)

    if multi:

        if len(posts) > 100 and message.channel.id == 624005677949517839:
            await bot.send("bruh that's way too many", message.channel)
            return
        elif len(posts) > 10 and message.channel.id != 624005677949517839:
            await bot.send("bruh that's way too many, send that in the spam", message.channel)
            return

        for post in posts:
            await handle_post(post, message, bot)
    else:
        await handle_post(posts[-1], message, bot)


async def handle_post(post, message, bot):

    try:  # attempt to get the data of the post
        data = post['data']
    except KeyError:  # if no data was found, than there is no post
        await bot.send("no posts found", message.channel)
        return

    if data['is_self']:  # if the post is marked as a selfpost
        print("self_post", data)
        embed = EmbedFactory.reddit_selfpost(data)

    else:
        try:  # check for a url
            link = data['url']
        except KeyError:  # if there is no url, then something is wrong; send a message and return
            await bot.send("Something went wrong!", message.channel)
            return

        print("Handling link:", link)
        link = UrlHandler.handle(link)  # see if UrlHandler can understand the link

        if not link:  # if UrlHandler failed (returns none, it's a link post)
            print("link_post", data)
            embed = EmbedFactory.reddit_link_post(data)

        else:  # if UrlHandler succeeded, it's an image post
            print("imagepost", data)
            embed = EmbedFactory.reddit_image_post(data, link)

    await bot.send("", message.channel, embed=embed)


async def stack(message, bot):
    arg = message.content.split(" ")

    try:
        if arg[1].lower() in ("yes", "true", "t", "1"):
            bot.stack = True
        else:
            bot.stack = False

    except IndexError:
        bot.stack = not bot.stack

    await bot.send("Changed `stack` to `" + str(bot.stack) + "`", message.channel)
    bot.update_subs()


async def handle_command(command, message, bot):

    try:
        method = command_list[command]
    except KeyError:
        method = default_command

    await method(message, bot)


async def handle_message(message, bot):

    if message.content.startswith(trigger):

        command = message.content.strip(trigger).split()[0]
        await handle_command(command, message, bot)

    else:

        try:
            int(message.content)
            await get_nhentai(message, bot)
            return
        except ValueError:
            await general(message, bot)


async def _help(message, bot):
    await bot.send(HELP_MESSAGE, message.channel)


async def ping(message, bot):

    ping_time = datetime.utcnow()

    message = await bot.send("Pinging...", message.channel)

    pong_time = datetime.utcnow()

    ping_milliseconds = (pong_time - ping_time) / timedelta(milliseconds=1)

    await message.edit(content="Ping: %d ms" % ping_milliseconds)


async def unknown_command(message, bot):
    await bot.send("Even Amadeus is confused! (by your command)", message.channel)


async def get_nhentai(message, bot):

    """try:
        if not message.channel.is_nsfw():
            await bot.send(NON_NSFW_WARNING, message.channel)
            return
    except AttributeError:
        pass"""

    gallery = nHentai.Gallery(message.content)

    await bot.send("", message.channel, embed=gallery.create_embed())


async def random_nhentai(message, bot):

    """try:
        if not message.channel.is_nsfw():
            await bot.send(NON_NSFW_WARNING, message.channel)
            return
    except AttributeError:
        pass"""

    gallery = nHentai.Gallery(nHentai.random())

    await bot.send("", message.channel, embed=gallery.create_embed())


async def nhentai_search(message, bot):

    """try:
        if not message.channel.is_nsfw():
            await bot.send(NON_NSFW_WARNING, message.channel)
            return
    except AttributeError:
        pass"""

    search_query = " ".join(message.content.split(" ")[1:])
    results = nHentai.search(search_query)

    await bot.send("", message.channel, embed=EmbedFactory.nhentai_gallery_list(search_query, results))


async def rule34_search(message, bot):

    """try:
        if not message.channel.is_nsfw():
            await bot.send(NON_NSFW_WARNING, message.channel)
            return
    except AttributeError:
        pass"""

    tags = " ".join(message.content.split(" ")[1:])

    try:
        number = int(tags)

        details = await r34_bot.getPostData(number)

        tags = details['@tags']
        image_url = details['@file_url']

        embed = EmbedFactory.rule34_image(tags, image_url, number)
        await bot.send("", message.channel, embed=embed)
        return

    except ValueError:

        links = await r34_bot.getImageURLS(tags)

        if not links:
            await bot.send("No posts found.", message.channel)

        embed = EmbedFactory.rule34_image([], random.choice(links), "Random result for " + tags)

        await bot.send("", message.channel, embed=embed)


async def forgotten_emote(message, bot):

    wanted_emote = " ".join(message.content.split(" ")[1:])

    if wanted_emote == "list":
        await bot.send("Current forgotten emotes:\n`" + " ".join(FORGOTTEN_IMAGES.keys()) + "`", message.channel)
        return

    try:

        await bot.send("", message.channel, file=FORGOTTEN_IMAGES[wanted_emote],
                       filename=FORGOTTEN_IMAGES[wanted_emote].split("\\")[-1])

    except KeyError:

        await bot.send("Unknown forgotten image", message.channel)


async def anime_search(message, bot):

    search_query = " ".join(message.content.split(" ")[1:])

    results = jikan.search('anime', search_query)['results']

    titles = [x['title'] for x in results]
    urls = [x['url'] for x in results]

    embed = EmbedFactory.MAL_search_result(titles, urls)

    await bot.send("", message.channel, embed=embed)


async def first_anime(message, bot):
    search_query = " ".join(message.content.split(" ")[1:])

    result = jikan.search('anime', search_query)['results'][0]

    title = result['title']
    link = result['url']
    image_url = result['image_url']
    synopsis = result['synopsis']

    embed = EmbedFactory.MAL_single_anime(title, link, image_url, synopsis)

    await bot.send("", message.channel, embed=embed)


async def add_quote(message, bot):

    new_quote = " ".join(message.content.split(" ")[1:])

    # Get the last message in the channel and use that as our quote
    if new_quote == "":

        quote_message = (await message.channel.history(limit=1, before=message).flatten())[0]

        new_quote = '"' + quote_message.content + '" - ' + quote_message.author.mention

    with open(QUOTES_PATH, 'a', encoding="utf-8") as file:
        file.write("\n")
        file.write(new_quote)

    await bot.send("Quote *"+ new_quote + "* added", message.channel)


async def get_quote(message, bot):

    quote_index = " ".join(message.content.split(" ")[1:])

    quote = "Something fucked up. Let <@234387706463911939> know."

    file = open(QUOTES_PATH, encoding="utf-8")

    if quote_index != "":

        try:
            quote_index = int(quote_index)
            # For the non programmers who don't use zero based index
            if quote_index > 0:
                quote_index -= 1
            elif quote_index == 0:
                raise IndexError

            quote = file.readlines()[quote_index]

        except ValueError or IndexError:
            quote = "I don't know that quote."

    else:
        quote = random.choice(file.readlines())

    await bot.send(quote, message.channel)


async def all_quotes(message, bot):

    await bot.send("Quotes",  message.channel, file=QUOTES_PATH, filename="quotes.txt")


def first_wikipedia(message, bot):
    search_query = " ".join(message.content.split(" ")[1:])

    result = wikipedia.search(search_query)[0]
    page = wikipedia.page(result)

    title = page.title
    summary = wikipedia.summary(result, chars=1024)
    url = page.url

    image_url = None
    if page.images:
        image_url = page.images[0]

    embed = EmbedFactory.wikipedia_article(title, summary, url, image_url)
    
    bot.send("", message.channel, embed=embed)
    
    
def create_r_bot():
    global r_bot

    with open('data//config.json') as json_data_file:
        r_data = json.load(json_data_file)['reddit']

        r_bot = RedditBot(r_data['username'], r_data['password'],
                          r_data['client-id'], r_data['secret-id'],
                          "DiscordScraper/v1.0")

    r_bot.authorize()


def create_r34_bot(loop):
    global r34_bot

    r34_bot = rule34.Rule34(loop)


command_list = {
    'stack': stack,
    'p': get_post,
    'help': _help,
    'pm': lambda m, b: get_post(m, b, multi=True),
    'ping': ping,
    'r': random_nhentai,
    's': nhentai_search,
    '34': rule34_search,
    'f': forgotten_emote,
    'search': anime_search,
    'anime': first_anime,
    'addquote': add_quote,
    'quote': get_quote,
    'quotes': all_quotes,
}

default_command = unknown_command

trigger = "/"


if __name__ == '__main__':
    rule34 = rule34.Sync()
    print(rule34.getImageURLS("lucina"))
    print(rule34.getPostData(1818))
