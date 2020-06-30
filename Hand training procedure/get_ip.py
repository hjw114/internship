import requests
def get_ip_info(ip):
  
              r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' %ip)              
              if  r.json()['code'] == 0 :
                            i = r.json()['data']
                            country = i['country']  #国家
                            area = i['area']        #区域
                            region = i['region']    #地区
                            city = i['city']        #城市
                            isp = i['isp']          #运营商
                            
                            print (u'国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, area, region, city, isp))
              else:
                            print ("ERROR! ip: %s" % ip)