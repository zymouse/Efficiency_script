#!/usr/bin/env python3
#！-*- coding:utf-8 -*-
"""
计算点的经纬度，并添加到文本中，生成新文本
"""
from re import L
from readline import parse_and_bind
from tokenize import Double
import yaml
from xml.dom.minidom import parse
from xml.etree.ElementTree import ElementTree

import xml.etree.ElementTree as ET
from xml.dom import minidom

from xml.dom.minidom import parseString

from pyproj import Transformer

import os

# 返回投影坐标系WKID号码--中国区域
def if_china_wgs84(Longitude):
    if(72 <= Longitude <= 138):
        '''
        32643	WGS_1984_UTM_Zone_43N
        32653	WGS_1984_UTM_Zone_53N
        '''
        return int(Longitude/6+31)+32600
    else:
        print("不是中国的经度")
        return -1


class OsmAddWgs84:
    def __init__(self):
        """
        self.collection.setAttribute("generator", 1111)      # 设置元素属性
        self.collection.hasAttribute("generator")            # 判断元素属性是否存在
        self.collection.getAttribute("generator")            # 获取元素属性
        self.collection.getElementsByTagName("node")         # 按标记表示获取元素
        """
        # yaml.warnings({'YAMLLoadWarning':False}) 
        with open(file="config.yaml",mode="r",encoding="utf-8") as f:
            # config = yaml.load(f)
            config = yaml.safe_load(f)
        # print(config["osm_file_inputPath"])

        with open(file=config["osm_file_inputPath"]+"origin.yaml",mode="r",encoding="utf-8") as f:
            # config = yaml.load(f)
            origin = yaml.safe_load(f)
            origin = origin["sensing"]["gnss"]["gnss_poser"]

        self.osm_file_outputPath = config["osm_file_outputPath"] + config["fileName"][0:-4] + "ok.osm"
        
        # print(config["osm_file_inputPath"]+config["fileName"])
        self.DOMTree = parse(config["osm_file_inputPath"]+config["fileName"])
        self.collection = self.DOMTree.documentElement
        print(self.DOMTree)

        # print ('collection属性',self.collection.nodeName,self.collection.nodeValue,self.collection.nodeType)

        self.utm_N=-1
        self.origin_lat = float(origin["origin_lat"])
        self.origin_lon = float(origin["origin_lon"])
        self.origin_alt = float(origin["origin_alt"])
        wgs84 = "epsg:4326"
        utm_wkid = if_china_wgs84(self.origin_lon)
        utm_N = utm_wkid
        self.transformer = Transformer.from_crs(wgs84, "epsg:"+str(utm_wkid))
        self.transformer_wgs = Transformer.from_crs("epsg:"+str(utm_N), wgs84)
        self.originUtmX = 0
        self.originUtmY = 0
        self.origin2utm()
        print(self.originUtmX)
        print(self.originUtmY)

        self.formot_parking_lot = '''

  <relation id="10001">
    <tag k="public_transport" v="stop_area" />
    <tag k="type" v="public_transport" />
  </relation>

    '''
        self.formot_coverage_path = '''

  <relation id="10000">
    <tag k="type" v="route"/>
    <tag k="subtype" v="road"/>
    <tag k="speed_limit" v="10"/>
    <tag k="location" v="urban"/>
    <tag k="one_way" v="yes"/>
  </relation>

    '''
        self.parking_lot_id=[]   # 自由区域ID
        self.coverage_path_id=[] # 遍历线段ID
        
        
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

    def relation_tag_parse(self, relation_obj):
        tags = relation_obj.getElementsByTagName('tag')
        for tag in tags:
            if tag.getAttribute("k") == "type":
                tag.setAttribute('v', 'route')

    def convert_element(self, element):
        return minidom.parseString(ET.tostring(element)).documentElement

    def way_tag_parse(self, way_obj):
        tags = way_obj.getElementsByTagName('tag')
        for tag in tags:
            if tag.getAttribute("k") == "type" and tag.getAttribute("v")=="parking_lot":
                self.parking_lot_id.append(way_obj.getAttribute("id"))

                nd_list = way_obj.getElementsByTagName('nd')
                last_tag_value = nd_list[0].getAttribute('ref')

                # 创建新的子元素
                new_tag = ET.SubElement(ET.Element('way'), 'nd')
                new_tag.set('ref', last_tag_value)

                # 在第一个nd元素之前插入新的子元素
                nd_list = way_obj.getElementsByTagName('tag')
                way_obj.insertBefore(self.convert_element(new_tag), nd_list[0])
                break
            if tag.getAttribute("k") == "type" and tag.getAttribute("v")=="coverage_path":
                self.coverage_path_id.append(way_obj.getAttribute("id"))

            

    def relation_add_root(self, formot_str, id_list):
        if len(id_list) != 0:
            new_element = ET.fromstring(formot_str)

            for id in id_list: 
                ET.SubElement(new_element, 'member', {'type': 'way', 'role': '', 'ref': id})
            
            new_element_str = ET.tostring(new_element, encoding='unicode')
            new_element_dom = parseString(new_element_str)
            self.collection.appendChild(new_element_dom.documentElement)
    
    def readXMLfile(self):
        # 给点添加经纬度
        for node in self.collection.getElementsByTagName("node"):
            self.nodeE_tagEParse(node)

        # 
        for funtionPoint in self.collection.getElementsByTagName("funtionPoint"):
            self.nodeE_tagEParse(funtionPoint)

        # 修改relation子标签中的值
        for relation in self.collection.getElementsByTagName("relation"):
            self.relation_tag_parse(relation)
        
        # way带有parking_lot属性的way，闭环
        for way in self.collection.getElementsByTagName("way"):
            self.way_tag_parse(way)

        # 在根标签中添加新的relation，属性值是只有区域
        self.relation_add_root(self.formot_parking_lot, self.parking_lot_id)
        self.relation_add_root(self.formot_coverage_path, self.coverage_path_id)
        # 写入新的XML
        if not os.path.exists(os.path.dirname(self.osm_file_outputPath)):
            os.makedirs(os.path.dirname(self.osm_file_outputPath))
        with open(self.osm_file_outputPath,'w',encoding='utf-8') as f:
            # self.DOMTree.writexml(f, indent='', addindent='', newl='', encoding='utf-8')
            self.DOMTree.writexml(f, indent='', encoding='utf-8')


    def origin2utm(self):
        self.originUtmX,self.originUtmY= self.wgs84ToUtm(self.origin_lon, self.origin_lat)
    

    # lanelet2地图点坐标(local_x,local_y)转换wgs84
    def lanelet2Pint_CoordinateToWgs84(self, point_local, utm_origin):
        # point_local lanelet2地图点坐标(local_x,local_y) 坐标
        # utm_origin lanelet2地图坐标系原点对于utm坐标
        lat = point_local.x + utm_origin.x
        lon = point_local.y + utm_origin.y
        return lat, lon


    def wgs84ToUtm(self, lon, lat):  
        
        # transformer = Transformer.from_crs(wgs84, "epsg:"+str(utm_wkid))
        x, y = self.transformer.transform(lat, lon)
        # print(x)
        # print(y)
        return x, y

    def utmToWgs84(self, x, y):
        # wgs84 = "epsg:4326"
        # transformer = Transformer.from_crs("epsg:"+str(self.utm_N), wgs84)
        lat, lon = self.transformer_wgs.transform(x, y)
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
    