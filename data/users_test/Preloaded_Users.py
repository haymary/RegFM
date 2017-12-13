import pickle
import os


fb_user_path = os.path.join(os.getcwd(), '../../data', 'users_test', 'fb_user')
vk_user_path = os.path.join(os.getcwd(), '../../data', 'users_test', 'vk_user')


def load_test_vk_user(name=''):
    if name == '':
        name = vk_user_path
    return pickle.load(open(name, "rb"))


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
