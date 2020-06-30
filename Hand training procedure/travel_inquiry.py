import requests
import json

city = input('请输入您要查询的城市：')

url = 'http://api.map.baidu.com/telematics/v3/travel_city?location=%s&ak' \
      '=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json' % city
rs = requests.get(url)
rs.dict = json.loads(rs.text)
error = rs.dict['error']
if error == 0:
    date = rs.dict['date']
    result_dict = rs.dict['result']
    cityname = result_dict['cityname']
    abstract = result_dict['abstract']
    description = result_dict['description']
    itineraries_list = result_dict['itineraries']    
    print('日期：%s  城市名称：%s  ' % (date, cityname))
    print('摘要：%s' % abstract)
    print('城市简介：%s' % description)
    for x_dict in itineraries_list:
        name = x_dict['name']
        description1 = x_dict['description']
        itineraries_list1 = x_dict['itineraries']
        print('```````````````````````````````')
        print('方式：%s' % name)
        print('方式要点：%s' % description1)
        print('```````````````````````````````')
        for y_dict in itineraries_list1:
            lx = y_dict['description']
            dinning = y_dict['dinning']
            accommodation = y_dict['accommodation']
            way_list = y_dict['path']
            print('路线信息：%s' % lx)
            print('')
            print('就餐信息：%s' % dinning)
            print('')
            print('住宿信息：%s' % accommodation)
            print('')
            for fengjing in way_list:
                fj_name = fengjing['name']
                print('行程的景点有：%s' % fj_name)
            print('```````````````````````````````')
else:
    print('信息不存在')
