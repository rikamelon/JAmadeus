import discord


def reddit_default(data):

    embed = discord.Embed()
    embed.set_author(name=data['title'], url="https://www.reddit.com" + data['permalink'])
    embed.title = "Link to thread"
    embed.url = "https://www.reddit.com" + data['permalink']
    embed.set_footer(text="by u/" + data['author'])
    embed.colour = 16733952

    if data['spoiler']:
        embed.description = "Spoiler Alert!\nClick the link to thread if you are interested!"
        return embed

    return embed


def reddit_selfpost(data):

    embed = reddit_default(data)

    if data['spoiler']:
        return embed

    # cap off maximum of 2048
    if len(data['selftext']) > 2048:
        data['selftext'] = data['selftext'][:2045] + "..."

    embed.description = data['selftext']

    return embed


def reddit_link_post(data):

    embed = reddit_default(data)

    if data['spoiler']:
        return embed

    embed.description = data['url']

    return embed


def reddit_image_post(data, image_link):

    embed = reddit_default(data)

    if data['spoiler']:
        return embed

    embed.set_image(url=image_link)

    return embed


def nhentai_gallery(_id, url, title, pages, tags, languages, artists, categories, parodies, characters, groups,
                    cover_url):

    tag_string = nhentai_tag_formatter(tags)

    embed = discord.Embed()
    embed.colour = 15476564

    embed.title = title

    if not ("lolicon" in tag_string or "shotacon" in tag_string):
        embed.set_thumbnail(url=cover_url)
        embed.url = url

        embed.set_author(name=_id, url=url)

    else:

        embed.set_author(name=_id)

    embed.add_field(name="Pages", value=pages)

    if tag_string:
        embed.add_field(name="Tags", value=tag_string)

    language_string = nhentai_tag_formatter(languages)
    if language_string:
        embed.add_field(name="Languages", value=language_string)

    artist_string = nhentai_tag_formatter(artists)
    if artist_string:
        embed.add_field(name="Artists", value=artist_string)

    categories_string = nhentai_tag_formatter(categories)
    if categories_string:
        embed.add_field(name="Categories", value=categories_string)

    parodies_string = nhentai_tag_formatter(parodies)
    if parodies_string:
        embed.add_field(name="Parodies", value=parodies_string)

    characters_string = nhentai_tag_formatter(characters)
    if characters_string:
        embed.add_field(name="Characters", value=characters_string)

    groups_string = nhentai_tag_formatter(groups)
    if groups_string:
        embed.add_field(name="Groups", value=groups_string)

    return embed


def nhentai_tag_formatter(tags):

    new_tags = []

    for i in tags:

        if i[0] != "lolicon" and i[0] != "shotacon":
            new_tags.append("[" + i[0] + "](https://nhentai.net" + i[2] + ") (" + str(i[1]) + ")\n")
        else:
            new_tags.append(i[0] + " (" + str(i[1]) + ")\n")

    tags = new_tags

    ret, left = list_maker(tags, 1020)

    if left != 0:
        ret += "+" + str(left) + " more"

    return ret


def nhentai_gallery_list(query, results):

    embed = discord.Embed()
    embed.colour = 15476564

    embed.set_author(name="Search results for: " + query)

    results = ["**" + x[0] + "** - " + x[1] + "\n" for x in results]

    embed.description = list_maker(results, 2048)[0]

    return embed


def rule34_image(tags, image_url, title):
    embed = discord.Embed()
    embed.colour = 11199907

    embed.set_author(name=str(title))
    embed.set_image(url=image_url)

    tag_string = list_maker(tags, 2048)[0]
    if tag_string:
        embed.add_field(name="Tags", value=tag_string)

    return embed


def blank(message):

    embed = discord.Embed()
    embed.description = message

    return embed


def list_maker(_list, _max):

    j = len(_list)

    ret = ""

    for i in _list:

        if len(i) + len(ret) > _max:
            return ret, j

        j -= 1
        ret += str(i)

    return ret, 0
