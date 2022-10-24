from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus
from dataclasses import dataclass
from typing import List


@dataclass
class Chunin:
    title: str
    description: str
    moves: list
    pic: str


def home_view(request):
    context = {

    'groups': {
        'Naruto': Chunin("Naruto", "Naruto is part of the Uzumaki clan, son of the 4th Hokage, and the Nine Tails jinchuriki. He is known as the hero of the Hidden Leaf Village and it is his dream to become the Hokage.", ["Brooks, Chevy, Errin, Kevin, Lukas, Andrew"], "images/naruto_background.jpg"),
        'Sasuke':  Chunin("Sasuke", "This team handles Base Camp's social media presence, they take pictures of events and post updates about what goes on at Base Camp.", ["Colt, Isaiah, Cooper, Cannon, Angela, Antonio, Gabriel"], "images/sasuke_background.jpg"),
        'Gaara':  Chunin("Gaara", "This team is in charge of all things food related at Base Camp. They buy groceries, order takeout, and cook lunch for fellow students and staff.", ["Mike, Dylan, Anna, Zaul, Luke, River"], "images/gaara_background5.png"),
        'Neji':  Chunin("Neji", "This team is in charge of planning events and activities for Base Camp students. They do things from planning bowling trips to running an afterschool program at Davidson Elementary School.", ["Joshua, Malcolm, Amber, J.W, Eric"], "images/gaara_background5.webp"),
        }
}
    return render(request, "home.html", context)


def detail_view(request, group):
    context = {
    'group': group,
    'context': {
        'Naruto': Chunin("Naruto", "Naruto is part of the Uzumaki clan, son of the 4th Hokage, and the Nine Tails jinchuriki. He is known as the hero of the Hidden Leaf Village and it is his dream to become the Hokage.", ["Rasengan, Wind-style Rasengan, Summoning Jutsu, Sage Mode, KCM, and Shadow Clones"], "images/naruto_background.jpg"),
        'Sasuke':  Chunin("Sasuke", "Sasuke is the last of the Uchiha clan and it is his life's goal to avenge their deaths. Leaving his friends and village behind, he lets nothing stand in the way of his quest for vengeance, even if it means he must journey into the darkness.", ["Sharingan, Chidori, Fireball Jutsu, Kirin, Susanoo, and Amaterasu"], "images/sasuke_background.jpg"),
        'Gaara':  Chunin("Gaara", "The One Tails jinchuriki was once feared as a demon, but has since changed his ways(inspired by Naruto) and become the leader of his village. Despite his monstrous and murderous past, he is now looked up to by many and strives to make the world one of peace.", ["Sand Coffin, Sand Mausoleum, Sand Burial, Sand Armor, and Sand Shield"], "images/gaara_background5.png"),
        'Neji':  Chunin("Neji", "Neji is part of the Hyuga clan. He was initially bound to beliefs of fate and destiny, but is now a symbol for change having overcome his 'fate'.", ["Byakugan, Gentle Fist, and Eight Trigrams Palm Variations"], "images/neji_background3.jpg"),
        }
}
    return render(request, "details.html",context)