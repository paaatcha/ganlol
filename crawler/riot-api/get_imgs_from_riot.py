#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: André Pacheco
E-mail: pacheco.comp@gmail.com

This script downloads the LOL splash arts using Riot API
"""

import requests as req
import os

# The riot's urls
# "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_0.jpg"
URL_SPLASH = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
URL_LOADING = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"

# The path you'd like to save the images
DATASET_PATH_SPLASHS = "/home/patcha/datasets/LOL/splash"
DATASET_PATH_LOADING = "/home/patcha/datasets/LOL/loading"

with open("../champions_name.txt","r") as f:
    champs = f.read().splitlines()

# looping through the champions and creating the URL
kth = 0
for champ in champs:

    while True:
        url_s = URL_SPLASH + champ + "_" + str(kth) + ".jpg"
        url_l = URL_LOADING + champ + "_" + str(kth) + ".jpg"

        path_s = os.path.join(DATASET_PATH_SPLASHS, "{}_{}.jpg".format(champ, kth))
        path_l = os.path.join(DATASET_PATH_LOADING, "{}_{}.jpg".format(champ, kth))

        try:

            # making the request for the splash art
            data_s = req.get(url_s, timeout=45)

            # making the request for the loading art
            data_l = req.get(url_l, timeout=45)

            # if the requisition is not ok, it means the image doesn't exist for the champ_kth
            if not data_s.ok:
                print("[NO] " + url_s.split("/")[-1] + " doesnt exist!")
                kth = 0
                break

            # saving the splash art
            with open(path_s, "wb") as f:
                f.write(data_s.content)

            # saving the loading art
            with open(path_l, "wb") as f:
                f.write(data_l.content)

            print("[YES] " + url_s.split("/")[-1] + " was downloaded")

        except:
            print("[ERROR] Something got wrong with " + url_s.split("/")[-1])

        kth += 1


