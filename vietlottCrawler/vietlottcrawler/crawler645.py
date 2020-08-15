from bs4 import BeautifulSoup
import requests
import json, os
import redis

url = 'https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-645?pageindex={}&nocatche=1'

redis_host = os.environ['REDIS_HOST']
redis_pw = os.environ['REDIS_PW']
redis_port = os.environ['REDIS_PORT']
redis_db = 0

def get_set_numbers(pageindex,snum):
    pageindex = pageindex
    snum = snum

    req = requests.get(url.format(pageindex))
    soup = BeautifulSoup(req.text, 'html.parser')

    day_so_ket_qua_v2 = soup.find_all("div",{'class':'day_so_ket_qua_v2'})
    all_td_bong_tron = day_so_ket_qua_v2[-8:]

    var_nums = []

    for i in all_td_bong_tron:

        content_span_1 = i.contents[snum].text
        var_nums.append(content_span_1)
    return(var_nums)

def store_set_numbers(key_name,set_number):

    r = redis.StrictRedis(host=redis_host, port=redis_port,
                          db=redis_db, password=redis_pw)
    print( "storing to redis: ",key_name )
    json_data = json.dumps(set_number)
    r.set(key_name, json_data)


def lambda_handler(event, context):

    num1 = get_set_numbers('0',1) + get_set_numbers('1',1) + get_set_numbers('2',1) + get_set_numbers('3',1)
    num1 = num1[2:]
    removed_dup_num1 = list(dict.fromkeys(num1))
    store_set_numbers('removed_dup_num1',removed_dup_num1)

    num2 = get_set_numbers('0',2) + get_set_numbers('1',2) + get_set_numbers('2',2) + get_set_numbers('3',2)
    num2 = num2[2:]
    removed_dup_num2 = list(dict.fromkeys(num2))
    store_set_numbers('removed_dup_num2',removed_dup_num2)

    num3 = get_set_numbers('0',3) + get_set_numbers('1',3) + get_set_numbers('2',3) + get_set_numbers('3',3)
    num3 = num3[2:]
    removed_dup_num3 = list(dict.fromkeys(num3))
    store_set_numbers('removed_dup_num3',removed_dup_num3)

    num4 = get_set_numbers('0',4) + get_set_numbers('1',4) + get_set_numbers('2',4) + get_set_numbers('3',4)
    num4 = num4[2:]
    removed_dup_num4 = list(dict.fromkeys(num4))
    store_set_numbers('removed_dup_num4',removed_dup_num4)

    num5 = get_set_numbers('0',5) + get_set_numbers('1',5) + get_set_numbers('2',5) + get_set_numbers('3',5)
    num5 = num5[2:]
    removed_dup_num5 = list(dict.fromkeys(num5))
    store_set_numbers('removed_dup_num5',removed_dup_num5)

    num6 = get_set_numbers('0',6) + get_set_numbers('1',6) + get_set_numbers('2',6) + get_set_numbers('3',6)
    num6 = num6[2:]
    removed_dup_num6 = list(dict.fromkeys(num6))
    store_set_numbers('removed_dup_num6',removed_dup_num6)