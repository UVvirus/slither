import json
import os
from zipfile import ZipFile
import shutil

def get_input():
    # with ZipFile(zip_file, 'r') as zip:
    #     zip.extractall('/home/you_we/PycharmProjects/slither_api_project/')
    #
    # with ZipFile(input_zip, 'r') as zip:
    #     dirname = input_zip.split('.')[0]
    #     zip.extractall(dirname)
    # zip.close()
    # source = '/home/you_we/PycharmProjects/slither_api_project/test_zip'
    # destination = '/home/you_we/ethernaut'
    # shutil.move(source,destination)
    # os.chdir(destination)
    # cmd = f"slither {dirname}/ --solc-remaps @openzeppelin/=$(pwd)/node_modules/@openzeppelin/  --json slither_out.json"
    # os.system(cmd)

    with open("small_output.json","r") as file:
       json_file = json.load(file)
    #print(json_file)
    description = json_file["results"]["detectors"][0]["description"]
    impact = json_file["results"]["detectors"][0]["impact"]
    empty_list=[]
    # result_dictionary = {"DESCRIPTION": description,
    #                      "IMPACT": impact
    #                      }
    result_dictionary = {}
    size = len(json_file["results"]["detectors"])
    # print(size)
    for i in range(0, size):
        description = json_file["results"]["detectors"][i]["description"]
        impact = json_file["results"]["detectors"][i]["impact"]
        result_dictionary["DESCRIPTION"]=description
        result_dictionary["IMPACT"]=impact
        empty_list.append(result_dictionary)
    file.close()
    #print(empty_list)
    return empty_list

        # print("DESCRIPTION:",description)
        # print("IMPACT:", impact)
        #print("=====================================================================================================")

    #file.close()


if __name__ == "__main__":
    get_input()