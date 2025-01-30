from dice import * 
import time 

threshold = 0.5

string_parameters_5 = '''"Support N3GPP": True,"Accuracy": 1,"DN": 0,"MM, Telephone": False,"Maximum number of PDU sessions": 1001,'''
full_json_5 = dice.replace_params_with_threshold(NEST,string_parameters_5,threshold=threshold,keyword_threshold=threshold)

string_parameters_10 = string_parameters_5 + '''"Maximum number of UEs": 100002,"N3GPP Support": False,"SSC": 1,"Guaranteed Rate of Downlink": 100004,"Guaranteed Rate of Uplink": 100003,'''
full_json_10 = dice.replace_params_with_threshold(NEST,string_parameters_10,threshold=threshold,keyword_threshold=threshold)

string_parameters_20 = string_parameters_10 + '''"Max Bit Rate of Downlink": 100002,"Max Bit Rate of Uplink": 100001,"Max Data Burts": 0.002,"Max Packet Loss Rate": 100001,"Delay Budget": 0.00010,"Error Rate": 0.0111,"Levels Priority": 0.5,"Is Shared": True,"Supported Data Network": "internets","Supported device velocity": 11,'''
full_json_20 = dice.replace_params_with_threshold(NEST,string_parameters_20,threshold=threshold,keyword_threshold=threshold)

string_parameters_40 = string_parameters_20 + '''"Synchronic": "JUST UEs","density of UEs": 10001,"availability": 0,"exposed": False,"shared": False,"gtp_Ip": "192.168.99.1","mcc": 201,"mnc": 91,"slices - sd": [{"sd": 66050 - "st": 2}],"idLength": 30,"ignoreStreamId": True,"link IP": "127.2.0.1","mcc": "207","mnc": "91","nci": "0x000000011","ngapIp": "127.1.0.1","supportDnnList": ["internets"],"routes": [{"name": "backhauls"}],"tac": 1,"replicas": 2'''
full_json_40 = dice.replace_params_with_threshold(NEST,string_parameters_40,threshold=threshold,keyword_threshold=threshold)