#!/usr/bin/env python
# -*- coding: cp936 -*-
# Author: Shunfa Zhang
# Date: 2016/2/22


allSet = set([
    "联想",
    "爱贝",
    "福利宝",
    "魅族",
    "百度移动",
    "安智市场",
    "鲤鱼",
    "朋友玩",
    "豌豆荚",
    "安锋",
    "指拇游玩",
    "华为",
    "腾讯应用宝游戏币",
    "小米",
    "UC",
    "腾讯应用宝",
    "当乐",
    "有玩",
    "靠谱助手",
    "机锋",
    "手盟",
    "搜狗",
    "七匣子",
    "优酷网游",
    "酷派",
    "电信爱游戏",
    "PPTV",
    "7k7k"
])


talkingDataSet = set([
    "360",
    "7k7k",
    "PPTV",
    "UC",
    "vivo",
    "七匣子",
    "优酷网游",
    "华为",
    "安智市场",
    "安锋",
    "小米",
    "当乐",
    "手盟",
    "指拇游玩",
    "搜狗",
    "有玩",
    "机锋",
    "爱贝",
    "电信爱游戏",
    "百度移动",
    "联想",
    "虫虫",
    "豌豆荚",
    "酷派",
    "靠谱助手",
    "魅族",
    "游久",
    "鲤鱼"
])

remindChannel = allSet - talkingDataSet

for value in remindChannel:
    print value

