"""
    create a function called "addPost()", which will take exactly 3 parameters: the list in which the post is to be added, the post title and the post body
    the function will form a new dictionary formed of the last 2 parameters and add it into the first place inside the first parameter
    the function will NOT return anything
"""
from os import system
system ("cls")

def addPost(post, title, body):
    # crearea noului dictionar
    add = {"title": title, "body": body}
    # aratam locul noului dict., il vom pune pe prima pozitie
    posts.insert(0, add)

posts = [
  {
  "title": "About the importance of functional programming",
  "body": "Functional programming is ....." 
  },
  {
  "title": "OOP programming brings classes and objects into the code",
  "body": "OOP is  ....." 
  },
]


#addPost(posts, "titlul_1", "body_1")
#print(posts)