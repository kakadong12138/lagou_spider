# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import traceback
import time
import re
import json
import copy
import json 


class ListSpider(scrapy.spiders.Spider):
    name = "list"
    allowed_domains = ["dianping.com"]
    handle_httpstatus_list = [404] 
    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Anit-Forge-Token":  "None",
        "X-Requested-With":   "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Content-Type" :   "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin" : "https://www.lagou.com",
        "X-Anit-Forge-Code" : "0",
        "Referer" :"https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput="
    }
    headers["Cookie"] = "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491740347,1491740410,1491740517; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491740548; _ga=GA1.2.1428612494.1491740347; _gat=1; user_trace_token=20170409201906-ba4dc1c2-1d1e-11e7-8049-525400f775ce; LGSID=20170409202156-1f9738a6-1d1f-11e7-9d7e-5254005c3644; PRE_UTM=; PRE_HOST=blog.csdn.net; PRE_SITE=http%3A%2F%2Fblog.csdn.net%2Fhk2291976%2Farticle%2Fdetails%2F51284576; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; LGRID=20170409202227-31f086a6-1d1f-11e7-9d7e-5254005c3644; LGUID=20170409201906-ba4dc768-1d1e-11e7-8049-525400f775ce; JSESSIONID=4EF78C10CBAB0971B76DB508C2557DD1; SEARCH_ID=32bf7b8af6f3400f841bd9cc312a2edb"


    def start_requests(self):
        key_words = ["python"]
        for key_word in key_words:
            url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"
            request = FormRequest(url,formdata={"first":"true","pn":"1","kd":key_word},headers=self.headers)
            yield request
        
       

    def parse(self,response):
        body_json = json.loads(response.body_as_unicode())
        print body_json.keys()







