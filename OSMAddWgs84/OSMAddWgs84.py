#!/usr/bin/env python3
#！-*- coding:utf-8 -*-
from re import L
from readline import parse_and_bind
from tokenize import Double
import yaml
from xml.dom.minidom import parse
from xml.etree.ElementTree import ElementTree
from pyproj import Transformer

class OsmAddWgs84:
    def __init__(self):
        # yaml.warnings({'YAMLLoadWarning':False}) 
        with open(file="config.yaml",mode="r",encoding="utf-8") as f:
            config = yaml.load(f)
        print(config["osm_file_inputPath"])

        self.osm_file_outputPath = config["osm_file_outputPath"]
        self.DOMTree = parse(config["osm_file_inputPath"])
        self.collection = self.DOMTree.documentElement
        print(self.DOMTree)

        # print ('collection属性',self.collection.nodeName,self.collection.nodeValue,self.collection.nodeType)

        """
        self.collection.setAttribute("generator", 1111)      # 设置元素属性
        self.collection.hasAttribute("generator")            # 判断元素属性是否存在
        self.collection.getAttribute("generator")            # 获取元素属性
        self.collection.getElementsByTagName("node")         # 按标记表示获取元素
        """
       
        
        self.utm_N=-1
        self.origin_lat = config["origin_lat"]
        self.origin_lon = config["origin_lon"]
        self.origin_alt = config["origin_alt"]

        self.originUtmX = 0
        self.originUtmY = 0
        self.origin2utm()
        print(self.originUtmX)
        print(self.originUtmY)


    
    # xml文件里，node元素的对象里，tag元素解析
    def nodeE_tagEParse(self, node):
        local_x = 0
        local_y = 0
        tags = node.getElementsByTagName('tag')
        for tag in tags:
            if tag.hasAttribute("k") and tag.hasAttribute("v"):
                key_name = tag.getAttribute("k")
                value_name = tag.getAttribute("v")  
                # print(value_name)  
                if(key_name=="local_x"):
                    local_x = float(value_name) + self.originUtmX
                if(key_name=="local_y"):
                    local_y = float(value_name) + self.originUtmY
        
        lat, lon = self.utmToWgs84(local_x, local_y)
        node.setAttribute("lat", str(lat)) 
        node.setAttribute("lon", str(lon))
                              
    def readXMLfile(self):
        for node in self.collection.getElementsByTagName("node"):
            self.nodeE_tagEParse(node)

        with open(self.osm_file_outputPath,'w',encoding='utf-8') as f:
            self.DOMTree.writexml(f, indent='', addindent='', newl='', encoding='utf-8')


    def origin2utm(self):
        self.originUtmX,self.originUtmY= self.wgs84ToUtm(self.origin_lon, self.origin_lat)
    

    # 返回投影坐标系WKID号码--中国区域
    def if_china_wgs84(self, Longitude):
        if(72 <= Longitude <= 138):
            '''
            32643	WGS_1984_UTM_Zone_43N
            32653	WGS_1984_UTM_Zone_53N
            '''
            return int(Longitude/6+31)+32600
        else:
            print("不是中国的经度")
            return -1

    # lanelet2地图点坐标(local_x,local_y)转换wgs84
    def lanelet2Pint_CoordinateToWgs84(self, point_local, utm_origin):
        # point_local lanelet2地图点坐标(local_x,local_y) 坐标
        # utm_origin lanelet2地图坐标系原点对于utm坐标
        lat = point_local.x + utm_origin.x
        lon = point_local.y + utm_origin.y
        return lat, lon


    def wgs84ToUtm(self, lon, lat):  
        # lon lat经纬度  alt 海拔高度
        wgs84 = "epsg:4326"
        utm_wkid = self.if_china_wgs84(lon)
        self.utm_N = utm_wkid
        transformer = Transformer.from_crs(wgs84, "epsg:"+str(utm_wkid))
        x, y = transformer.transform(lat, lon)
        # print(x)
        # print(y)
        return x, y

    def utmToWgs84(self, x, y):
        wgs84 = "epsg:4326"
        transformer = Transformer.from_crs("epsg:"+str(self.utm_N), wgs84)
        lat, lon = transformer.transform(x, y)
        return lat, lon

if __name__ == "__main__":
    xmlObj = OsmAddWgs84()
    xmlObj.readXMLfile()
    # a = xmlObj.wgs84ToUtm(106.668773828569, 26.7487259482772)
    
    # a= 0
    # for i in (0,1):
    #     if(1):
    #         if (1):
    #             a = 1
    # print(a)
    