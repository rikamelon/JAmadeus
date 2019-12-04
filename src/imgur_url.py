import re
import requests


def get_imgur_urls(starturl):
    '''
    Scans which kind of imgur url the link is and used the correct
    function for returning it.
    '''

    albumRegEx = r"imgur.com\/a\/([\w\d]*)"
    galleryRegEx = r"imgur.com\/gallery\/([\w\d]*)"
    singleImageRegEx = r"imgur.com\/([\w\d]{7})"

    if re.search(albumRegEx, starturl.replace(' ', '')):
        return get_album_urls(starturl.replace(' ', ''))
    elif re.search(galleryRegEx, starturl.replace(' ', '')):
        return get_album_urls(starturl.replace(' ', ''))
    elif re.search(singleImageRegEx, starturl.replace(' ', '')):
        return get_single_image_url(starturl.replace(' ', ''))
    else:
        raise ValueError('Not an valid imgur link!')


def get_album_urls(starturl):
    return starturl, -1


def get_gallery_urls(starturl):
    return starturl, -1


def get_single_image_url(starturl):
    finishedurl = []
    regex = r"href\=\"https://i\.imgur\.com\/([\d\w]*)(\.jpg|\.png|\.gif|\.mp4|\.gifv)"
    try:
        imgurHTML = requests.get(starturl)
    except:
        raise Exception('Something failed with the download')

    imgurhash = re.findall(regex, imgurHTML.text)
    finishedurl.append('https://i.imgur.com/{0}{1}'.format(imgurhash[0][0], imgurhash[0][1]))
    return finishedurl[0], 1


'''
Test URLS:
Album: https://imgur.com/a/3aeC1

SingleImage: https://imgur.com/URyijAU

Gallery: https://imgur.com/gallery/sQJ2h
'''