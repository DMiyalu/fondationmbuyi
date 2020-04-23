from django.http import Http404

class Article():

    LIST = [
		{'id': 1, 'titre': "Premier post", 'contenu': "Lorem ipsum dolor sit amet consectetur."},
		{'id': 2, 'titre': "Deuxieme post", 'contenu': "Lorem ipsum dolor sit amet consectetur."},
		{'id': 3, 'titre': "Troisième post", 'contenu': "Lorem ipsum dolor sit amet consectetur."},
	]


    @classmethod
    def all(cls):
        return cls.LIST



    @classmethod
    def findById(cls, id):
        try:
            return cls.LIST[int(id) - 1]
        except:
            raise Http500('')


    
