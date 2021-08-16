#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import parse
import requests
from json import loads
geo_api_url = 'https://restapi.amap.com/v3/geocode/geo?key=be8762efdce0ddfbb9e2165a7cc776bd&s=rsv3&language=zh_cn&extensions=base&appname=https%3A%2F%2Fxg.hit.edu.cn%2Fzhxy-xgzs%2Fxg_mobile%2FxsMrsbNew&csid=47204181-378A-4F55-A94D-548A5BFD0DFD&sdkversion=1.4.16&address='
regeo_api_url = 'https://restapi.amap.com/v3/geocode/regeo?key=be8762efdce0ddfbb9e2165a7cc776bd&s=rsv3&language=zh_cn&extensions=base&appname=https%3A%2F%2Fxg.hit.edu.cn%2Fzhxy-xgzs%2Fxg_mobile%2FxsMrsbNew&csid=47204181-378A-4F55-A94D-548A5BFD0DFD&sdkversion=1.4.16&location='
# 125.136835,46.580384
addr = input('输入您所在具体位置，格式：(X国)XX省XX市XX区XXXX，如黑龙江省哈尔滨市南岗区哈尔滨工业大学\n')
addr = parse.quote(addr)
geo_response = requests.get(geo_api_url+addr)
location = geo_response.json()['geocodes'][0]['location']
addr_spl = location.split(',')
longitude, latitude = addr_spl[0], addr_spl[1]
regeo_response = requests.get(regeo_api_url+location)
geo_info = regeo_response.json()['regeocode']
addr = geo_info['formatted_address']
addr_component = geo_info['addressComponent']
province = addr_component['province']
city = addr_component['city']
district = addr_component['district']
street_number = addr_component['streetNumber']
street_number = street_number['street']+street_number['number']
post_data = '''
{
    // 经典🐂🐎外包项目，拼音+天书命名变量，没🐎
    "gpsjd": '''+str(longitude)+''', //【所有人需要填写】，经度，不加引号，中国地区都是正实数。
    "gpswd": '''+str(latitude)+''', //【所有人需要填写】，纬度，不加引号。中国地区都是正实数。
    "jzdz": "", //居住地址，仅走读需要填写
    "kzl1": "1", //1-国内，0-国外
    "kzl2": "", //国外的国家和地区
    "kzl3": "", //国外的城市
    "kzl4": "", //国外具体地址
    "kzl5": "", //是否30日内回国：0-否，1-是，正常无需填写
    "kzl6": "'''+province+'''", //【所有人需要填写】所在省
    "kzl7": "'''+city+'''", //【所有人需要填写】所在市
    "kzl8": "'''+district+'''", //【所有人需要填写】所在区
    "kzl9": "'''+street_number+'''", //【所有人需要填写】所在街道+门牌号
    "kzl10": "'''+addr+'''", //【所有人需要填写】具体地址
    "kzl11": "", //与上次定位在不同城市的原因；0-探亲，1-旅游，2-回家，3-出差实习；4-其它
    "kzl12": "", //具体原因
    "kzl13": "0", //【所有人需要填写】当前地区风险等级0-低，1-中，2-高
    "kzl14": "", //所处中/高风险地区所在街道，社区名称
    "kzl15": "0", //【所有人需要填写】当日是否途径中高风险地区0-否，1-是
    "kzl16": "", //途径中/高风险地区所在街道，社区名称
    "kzl17": "1", //【所有人需要填写】今日体温0-不正常，1-正常
    "kzl18": "0;", //【所有人需要填写】今日是否出现不适（多选），0-无不适，1-乏力，2-干咳，3-呼吸困难，4-其它
    "kzl19": "", //是否到相关医院或门诊检查
    "kzl20": "", //检查结果，0-疑似，1-确诊，2-其它
    "kzl21": "", //自行采取的救护措施，0-服药，1-未服药，2-其它
    "kzl22": "", //kzl21其它
    "kzl23": "0", //【所有人需要填写】当前健康情况：0-正常，1-无症状感染者，2-确诊病例
    "kzl24": "0", //【所有人需要填写】是否隔离：0-否，1-是
    "kzl25": "", //隔离场所0-医院，1-集中隔离点，2-家
    "kzl26": "", //隔离详细地址
    "kzl27": "", //隔离开始时间，yyyy-M-dd
    "kzl28": "0", //【所有人需要填写】本人或共同居住的家人是否与确诊病例、无症状感染者、疑似病例行程轨迹有交集，0-否，1-是
    "kzl29": "", //是否与确诊病例、无症状感染者乘坐同次航班和列车：0-否，1-是
    "kzl30": "", //详细说明
    "kzl31": "", //本人48小时内是否已进行核酸检测：0-否，1-是
    "kzl32": "2", //【所有人需要填写】目前本人新冠疫苗接种情况：0-未接种，1-部分接种，2-完全接种
    "kzl33": "", //其它
    "kzl34": {}, //kzl20其它
    "kzl38": "'''+province+'''", //【所有人需要填写】=kzl6
    "kzl39": "'''+city+'''", //【所有人需要填写】=kzl7
    "kzl40": "'''+district+'''" //【所有人需要填写】=kzl8
}
'''
with open('post_data.jsonc','w',encoding='utf-8') as f:
    f.write(post_data)
print('已生成上报信息至：post_data.jsonc，请仔细检查后再使用！')