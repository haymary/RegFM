import pickle
import os


def load_test_vk_user(name=''):
    return pickle.load(open(name, "rb"))


fb_user_path = os.path.join(os.getcwd(), 'data', 'test_users', 'fb_user')


def load_test_fb_user(name=''):
    if name == '':
        name = fb_user_path
    
    return pickle.load(open(name, "rb"))


def save_test_vk_user(u, name=''):
    if name != '': name = '_' + name
    pickle.dump(u, open("vk_user" + name, "wb"))


def save_test_fb_user(u, name=''):
    if name != '': name = '_' + name
    pickle.dump(u, open("fb_user" + name, "wb"))