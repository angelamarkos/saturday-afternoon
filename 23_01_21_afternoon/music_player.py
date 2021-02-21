import os
import uuid

class Person:
    FILE_PATH = os.path.normpath('./data/persons.txt')
    def __init__(self, first_name, last_name, email, password=None, profile_pic_url=None, birth_date=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password or Person.generate_password()
        self.__profile_pic_url = profile_pic_url
        self.__birth_date = birth_date

        self.validate()

    def validate(self):
        if not '@' in self.__email:
            raise('Input email with correct format.')

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__first_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    def edit(self, **kwargs):
        person_dict = self.__dict__
        for k, v in kwargs.items():
            print(hasattr(Person, k))
            if hasattr(Person, k):
                setattr(Person, k, v)

    def save(self):
        person_dict = self.__dict__
        with open(Person.FILE_PATH, 'a') as df:
            df.writeline(str(person_dict))

    @staticmethod
    def create(**kwargs):
        person = Person(**kwargs)
        person.save()

    def deactivate(self):
        self.is_active = False

    def __del__(self):
        pass

    @staticmethod
    def get(email):
        with open(Person.FILE_PATH, 'r') as df:
            line = df.readline()
            while line:
                if email in line:
                    return Person(**eval(line))


    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.__email}'

    @staticmethod
    def generate_password():
        pass

class Song:
    def __init__(self, title, artist, genre, duration, album):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.album = album
        self.id = uuid.uuid3(name=f'{self.title}_{self.artist}')

        self.__view = 0

    def play(self):
        self.__view += 1

    def save(self):
        pass

    @staticmethod
    def filter(self):
        pass



class Playlist:
    def __init__(self, title: str, songs: list, created_by: Person):
        self.title = title
        self.songs = songs
        self.created_by = created_by

    def add_song(self, song: Song, current_user):
        pass

    def follow_playlist(self, person):
        pl = PersonPlaylist(person, self)
        pl.save()

    def __add__(self, other):
        pass

class PersonPlaylist:
    def __init__(self, person: Person, playlist: Playlist):
        self.person = person
        self.playlist = playlist

    def save(self):
        pass



if __name__ == '__main__':
    person_info = input('Input persons f-name, l-name, email, password, prof_pic_url, birth_date: ').split(',')
    # person_info_2 = input('Input persons f-name, l-name, email, password, prof_pic_url, birth_date: ').split(',')
    person_1 = Person(*person_info)
    print(person_1)

    person_first_name = input('Input to update person_1  f-name: ')
    person_email = input('Input to update person_1  email: ')
    person_1.edit(first_name=person_first_name, email=person_email)
    print(person_1)
    person_1.save()
    person_1 = Person.get(email='test@sd')
    print(person_1)

