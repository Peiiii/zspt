import os, shutil, glob, uuid, random, time, json, inspect, functools, hashlib


def generate_hash(string):
    hex = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return hex


def generate_hash_number(string, length=20):
    hex = generate_hash(string)
    return int(hex, 16) % (10 ** length)


def generate_salt(length=32):
    assert length <= 32
    return uuid.uuid4().hex[:length]


def generate_random_id():
    return uuid.uuid4().hex


def generate_password_hash_secure(password):
    salt = generate_salt()
    hashed = generate_hash(password + salt)
    return hashed, salt


def generate_password_hash(password):
    salt = generate_hash('salt:' + password)
    return generate_hash(password + ':' + salt)


def check_password_hash(pwhash, password):
    salt = generate_hash('salt:' + password)
    hashed = generate_hash(password + ':' + salt)
    return hashed == pwhash
