import random


def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                # collision occured
                break

        print(
            f'{buckets} buckets, {tries} hashes before collison. ({tries / buckets:.1%})')


how_many_before_collision(1000)
