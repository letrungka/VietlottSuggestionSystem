import json, os
import random
import redis

redis_host = os.environ['REDIS_HOST']
redis_pw = os.environ['REDIS_PW']
redis_port = os.environ['REDIS_PORT']
redis_host = '34.201.31.21'
redis_port = '6739'
redis_pw = 'passwordVietlott'
redis_db = 1


def get_set_numbers(key_name):

    r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, password=redis_pw)
    print( "Retrieving to redis: ",key_name )
    list_data = json.loads(r.get(key_name))

    return list_data

numS1 = get_set_numbers('removed_dup_num1_655')
numS2 = get_set_numbers('removed_dup_num2_655')
numS3 = get_set_numbers('removed_dup_num3_655')
numS4 = get_set_numbers('removed_dup_num4_655')
numS5 = get_set_numbers('removed_dup_num5_655')
numS6 = get_set_numbers('removed_dup_num6_655')
numS7 = get_set_numbers('removed_dup_num7_655')

def random_func():

    s1 = random.choices(numS1, weights=None, cum_weights=None, k=1)[0]
    s2 = random.choices(numS2, weights=None, cum_weights=None, k=1)[0]
    s3 = random.choices(numS3, weights=None, cum_weights=None, k=1)[0]
    s4 = random.choices(numS4, weights=None, cum_weights=None, k=1)[0]
    s5 = random.choices(numS5, weights=None, cum_weights=None, k=1)[0]
    s6 = random.choices(numS6, weights=None, cum_weights=None, k=1)[0]
    s7 = random.choices(numS7, weights=None, cum_weights=None, k=1)[0]

    result = (s1,s2,s3,s4,s5,s6,s7)

    return result
 
def lambda_handler(event, context):
    response = []
    for i in range(5):
        a = random_func()
        response.append(a)

    print(response)
    return (response)


lambda_handler(event=None, context=None)
