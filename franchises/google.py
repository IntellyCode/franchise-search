import googlesearch as s
import word as w
def search(x):
    for j in s.search(x,lang='en'):
        w.word(j,"franch")
        print(j)
