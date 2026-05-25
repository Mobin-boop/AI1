"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Branch: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Implementing Informed and Uninformed Search Algorithms for a
Fully Observable, Deterministic, Sequential, Static, Discrete, Multi-Agent Environment
"""



from env import play
from search.a_star import a_star
from search.bfs import bfs
from search.dls import dls
from search.ucs import ucs


if __name__ == "__main__":
    play("easy-no-weapon",a_star , delay=200)
    # play("medium-no-weapon",a_star , delay=200)
    # play("hard-no-weapon",a_star , delay=200)
    # play("easy-no-weapon",bfs , delay=200)
    # play("medium-no-weapon",bfs , delay=200)
    # play("hard-no-weapon",bfs , delay=200)
    # play("easy-no-weapon",ucs , delay=200)
    # play("medium-no-weapon",ucs , delay=200)
    # play("hard-no-weapon",ucs , delay=200)
    # play("easy-no-weapon",dls , delay=200)
    # play("medium-no-weapon",dls , delay=200)#:/یکم طول میکشه باز بشه 
    # play("hard-no-weapon",dls , delay=200)#:/باز نمیشه  بیخیال این خدایی