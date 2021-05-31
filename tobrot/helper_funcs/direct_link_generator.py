# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Helper Module containing various sites direct links generators. This module is copied and modified as per need
from https://github.com/AvinashReddy3108/PaperplaneExtended . I hereby take no credit of the following code other
than the modifications. See https://github.com/AvinashReddy3108/PaperplaneExtended/commits/master/userbot/modules/direct_links.py
for original authorship. """

import json
import re
import math
import lk21
import urllib.parse
from os import popen
from random import choice
from js2py import EvalJs
import requests
from bs4 import BeautifulSoup

from tobrot.helper_funcs.exceptions import DirectDownloadLinkException

# def direct_link_generator(text_url: str):
#     """ direct links generator """
#     if not text_url:
#         raise DirectDownloadLinkException("`No links found!`")
#     elif 'zippyshare.com' in text_url:
#         return zippy_share(text_url)
#     elif 'yadi.sk' in text_url:
#         return yandex_disk(text_url)
#     elif 'cloud.mail.ru' in text_url:
#         return cm_ru(text_url)
#     elif 'mediafire.com' in text_url:
#         return mediafire(text_url)
#     elif 'uptobox.com' in text_url:
#         return uptobox(text_url)
#     elif 'osdn.net' in text_url:
#         return osdn(text_url)
#     elif 'github.com' in text_urls:
#         return github(text_url)
#     elif 'racaty.net' in text_url:
#         return racaty(text_url)
#     elif 'letsupload.io' in text_url:
#         return letsupload(text_url)
#     elif 'hxfile.co' in text_url:
#         return hxfile(text_url)
#     elif 'files.im' in text_url:
#         return filesim(text_url)
#     elif 'sbembed.com' in text_url:
#         return sbembed(text_url)
#     elif 'anonfiles.com' in text_url:
#         return anonfiles(text_url)
#     else:
#         raise DirectDownloadtext_urlException(
#             f'No Direct text_url function found for {text_url}')


def direct_link_generator(link: str):
    """ direct links generator """
    if not link:
        raise DirectDownloadLinkException("`No links found!`")
    elif 'zippyshare.com' in link:
        return zippy_share(link)
    elif 'yadi.sk' in link:
        return yandex_disk(link)
    elif 'cloud.mail.ru' in link:
        return cm_ru(link)
    elif 'mediafire.com' in link:
        return mediafire(link)
    elif 'uptobox.com' in link:
        return uptobox(link)
    elif 'osdn.net' in link:
        return osdn(link)
    elif 'github.com' in links:
        return github(link)
    elif 'racaty.net' in link:
        return racaty(link)
    elif 'letsupload.io' in link:
        return letsupload(link)
    elif 'hxfile.co' in link:
        return hxfile(link)
    elif 'files.im' in link:
        return filesim(link)
    elif 'sbembed.com' in link:
        return sbembed(link)
    elif 'anonfiles.com' in link:
        return anonfiles(link)
    else:
        raise DirectDownloadLinkException(
            f'No Direct link function found for {link}')


def zippy_share(url: str) -> str:
    link = re.findall("https:/.(.*?).zippyshare", url)[0]
    response_content = (requests.get(url)).content
    bs_obj = BeautifulSoup(response_content, "lxml")

    try:
        js_script = bs_obj.find("div", {"class": "center", }).find_all(
            "script"
        )[1]
    except:
        js_script = bs_obj.find("div", {"class": "right", }).find_all(
            "script"
        )[0]

    js_content = re.findall(r'\.href.=."/(.*?)";', str(js_script))
    js_content = 'var x = "/' + js_content[0] + '"'

    evaljs = EvalJs()
    setattr(evaljs, "x", None)
    evaljs.execute(js_content)
    js_content = getattr(evaljs, "x")

    return f"https://{link}.zippyshare.com{js_content}"


def racaty(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*racaty\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Racaty links found`\n")
    reqs = requests.get(link)
    bss = BeautifulSoup(reqs.text, 'html.parser')
    op = bss.find('input', {'name': 'op'})['value']
    id = bss.find('input', {'name': 'id'})['value']
    rep = requests.post(link, data={'op': op, 'id': id})
    bss2 = BeautifulSoup(rep.text, 'html.parser')
    dl_url = bss2.find('a', {'id': 'uniqueExpirylink'})['href']
    return dl_url


def letsupload(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*letsupload\.io\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Letsupload links found`\n")
    bypasser = lk21.Bypass()
    dl_url = bypasser.bypass_url(link)
    return dl_url


def sbembed(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*sbembed\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No SBembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url = bypasser.bypass_url(link)
    return dl_url


def hxfile(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*hxfile\.co\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No HXFile links found`\n")
    bypasser = lk21.Bypass()
    dl_url = bypasser.bypass_url(link)
    return dl_url


def filesim(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*files\.im\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No files.im links found`\n")
    bypasser = lk21.Bypass()
    dl_url = bypasser.bypass_url(link)
    return dl_url


def anonfiles(url: str) -> str:
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*anonfiles\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No links found`\n")
    bypasser = lk21.Bypass()
    dl_url = bypasser.bypass_url(link)
    return dl_url


def yandex_disk(url: str) -> str:
    """ Yandex.Disk direct links generator
    Based on https://github.com/wldhx/yadisk-direct"""
    try:
        link = re.findall(r'\bhttps?://.*yadi\.sk\S+', url)[0]
    except IndexError:
        reply = "`No Yandex.Disk links found`\n"
        return reply
    api = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    try:
        dl_url = requests.get(api.format(link)).json()['href']
        return dl_url
    except KeyError:
        raise DirectDownloadLinkException(
            "`Error: File not found / Download limit reached`\n")


def cm_ru(url: str) -> str:
    """ cloud.mail.ru direct links generator
    Using https://github.com/JrMasterModelBuilder/cmrudl.py"""
    reply = ''
    try:
        link = re.findall(r'\bhttps?://.*cloud\.mail\.ru\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No cloud.mail.ru links found`\n")
    command = f'vendor/cmrudl.py/cmrudl -s {link}'
    result = popen(command).read()
    result = result.splitlines()[-1]
    try:
        data = json.loads(result)
    except json.decoder.JSONDecodeError:
        raise DirectDownloadLinkException("`Error: Can't extract the link`\n")
    dl_url = data['download']
    return dl_url


def uptobox(url: str) -> str:
    """ Uptobox direct links generator
    based on https://github.com/jovanzers/WinTenCermin """
    try:
        link = re.findall(r'\bhttps?://.*uptobox\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Uptobox links found`\n")
    if UPTOBOX_TOKEN is None:
        logging.error('UPTOBOX_TOKEN not provided!')
        dl_url = url
    else:
        try:
            link = re.findall(r'\bhttp?://.*uptobox\.com/dl\S+', url)[0]
            logging.info('Uptobox direct link')
            dl_url = url
        except:
            file_id = re.findall(r'\bhttps?://.*uptobox\.com/(\w+)', url)[0]
            file_link = 'https://uptobox.com/api/link?token=%s&file_code=%s' % (
                UPTOBOX_TOKEN, file_id)
            req = requests.get(file_link)
            result = req.json()
            dl_url = result['data']['dlLink']
    return dl_url


def mediafire(url: str) -> str:
    """ MediaFire direct links generator """
    try:
        link = re.findall(r'\bhttps?://.*mediafire\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No MediaFire links found`\n")
    page = BeautifulSoup(requests.get(link).content, 'lxml')
    info = page.find('a', {'aria-label': 'Download file'})
    dl_url = info.get('href')
    return dl_url


def osdn(url: str) -> str:
    """ OSDN direct links generator """
    osdn_link = 'https://osdn.net'
    try:
        link = re.findall(r'\bhttps?://.*osdn\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No OSDN links found`\n")
    page = BeautifulSoup(
        requests.get(link, allow_redirects=True).content, 'lxml')
    info = page.find('a', {'class': 'mirror_link'})
    link = urllib.parse.unquote(osdn_link + info['href'])
    mirrors = page.find('form', {'id': 'mirror-select-form'}).findAll('tr')
    urls = []
    for data in mirrors[1:]:
        mirror = data.find('input')['value']
        urls.append(re.sub(r'm=(.*)&f', f'm={mirror}&f', link))
    return urls[0]


def github(url: str) -> str:
    """ GitHub direct links generator """
    try:
        re.findall(r'\bhttps?://.*github\.com.*releases\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No GitHub Releases links found`\n")
    download = requests.get(url, stream=True, allow_redirects=False)
    try:
        dl_url = download.headers["location"]
        return dl_url
    except KeyError:
        raise DirectDownloadLinkException("`Error: Can't extract the link`\n")


def wget_dl(url: str) -> str:
    try:
        print("Downloading Started")
        # i was facing some problem in filename That's Why i did this ,
        #  i will fix it later :(

        filename = os.path.basename(url)
        output = subprocess.check_output("wget '-r -nH --cut-dirs=7 --no-parent -A' '--output-document' '{}' '{}' ".format(
            filename, url), stderr=subprocess.STDOUT, shell=True)

        print("Downloading Complete", filename)
        return filename
    except KeyError:
        raise DirectDownloadLinkException("`Error: Can't extract the link`\n")

        return "error", filename


def useragent():
    """
    useragent random setter
    """
    useragents = BeautifulSoup(
        requests.get(
            'https://developers.whatismybrowser.com/'
            'useragents/explore/operating_system_name/android/').content,
        'lxml').findAll('td', {'class': 'useragent'})
    user_agent = choice(useragents)
    return user_agent.text
