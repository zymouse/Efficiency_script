#!/usr/bin/env python3
#！-*- coding:utf-8 -*-
from re import L
import yaml
from xml.dom.minidom import parse
import xml.dom.minidom
from pyproj import Transformer

class OsmAddWgs84:
    def __init__(self):
        yaml.warnings({'YAMLLoadWarning':False}) 
        with open(file="config.yaml",mode="r",encoding="utf-8") as f:
            config = yaml.load(f)
        print(config["osm_file_inputPath"])

        DOMTree = xml.dom.minidom.parse(config["osm_file_inputPath"])
        collection = DOMTree.documentElement
        self.xmlNodesObj = collection.getElementsByTagName("node")

        self.utm_N=-1

    def readXMLfile(self):
        for node in self.xmlNodesObj:
            # print ("*****Movie*****")
            # if movie.hasAttribute("title"):
            #     print ("Title: %s" % movie.getAttribute("title"))
            if node.hasAttribute("id"):
                print("id={}-------".format(node.getAttribute("id")))
            tags = node.getElementsByTagName('tag')
            for tag in tags:
                # print ("\tFormat: %s" % tag.getAttribute("k"))
                if tag.hasAttribute("k") and tag.hasAttribute("v"):
                    key_name = tag.getAttribute("k")
                    value_name = tag.getAttribute("v")
                    if(key_name == "local_x" or key_name == "local_y" or key_name == "ele"):
                        print("\t{}: {}".format(key_name, value_name))
    


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
        transformer = Transformer.from_crs(wgs84, "epsg:"+utm_wkid)
        self.utm_N = utm_wkid
        x, y = transformer.transform(lat, lon)
        return x, y

    def utmToWgs84(self, x, y):
        wgs84 = "epsg:4326"
        transformer = Transformer.from_crs("epsg:"+self.utm_N, wgs84)
        lat, lon = transformer.transform(x, y)
        return lat, lon

if __name__ == "__main__":
    xmlObj = OsmAddWgs84()
    xmlObj.readXMLfile()
    