from data.models import Trainer
from typing import List

def trainer_count():
    return 23

def selected_trainers(count: int):
    return [Trainer(id = 2,
                    name = 'Alberta Almeida',
                    expertise = 'Programação Web',
                    presentation = 'Apresentação aqui',
                    twitter = 'https://twitter.com/alberta_almeida',
                    facebook = 'https://facebook.com/almeidaalberta',
                    instagram = 'https://instagram.com/albermeida',
                    linkedin = 'https://linkedin.com/prof_alberta'),
            Trainer(id = 3,
                    name = 'Augusto Avillez',
                    expertise = 'Marketing',
                    presentation = 'Uma apresentação pessoal aqui',
                    twitter = 'https://twitter.com/augusto_avillez',
                    facebook = 'https://facebook.com/augustoavillez',
                    instagram = 'https://instagram.com/augillez',
                    linkedin = 'https://linkedin.com/prof_augusto'),
            Trainer(id = 1,
                    name = 'Osmar Tello',
                    expertise = 'Gestão de Conteúdos',
                    presentation = 'Uma apresentação aqui',
                    twitter = 'https://twitter.com/osmar_tello',
                    facebook = 'https://facebook.com/osmartello',
                    instagram = 'https://instagram.com/osmello',
                    linkedin = 'https://linkedin.com/prof_osmar')
            ][:count]