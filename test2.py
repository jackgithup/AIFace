# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8') 


import base64
import json
import requests

class AI(object):
    def __init__(self):
        pass

    # token = '{"refresh_token":"25.484280d298ff3204c39edc14e630b839.315360000.1867327192.282335-15708099","expires_in":2592000,"session_key":"9mzdCXCQFa0a+SnyZziPl7SBzp3ClvnYqZVnOqUbFh018mjkQAMoeZae3sfo+e5lj4cKFkJW70yqk4iWh\/5XRP6s2HAEaQ==","access_token":"24.2f23b20189c46096992eb6938541b84a.2592000.1554559192.282335-15708099","scope":"public brain_all_scope vis-faceverify_faceverify_h5-face-liveness vis-faceverify_FACE_V3 wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi","session_secret":"58ff2e18ea2ba05246de1d5107e1d083"}'
    def return_token(self):
        ak = 'X7cVXoMmrf0EfVBd8TeLNu7N'
        sk = 'vnI0ymOr6TRD09eoFkPHrBMmTCkHxE9y'
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak,sk)
        response = requests.post(host)
        res = json.loads(response.text)
        refresh_token = dict(res)["refresh_token"]
        # print(refresh_token)
        return refresh_token

    def get_img_base(self,file):
        with open(file, 'rb') as fp:
            content = base64.b64encode(fp.read())
        return content

    def get_socre(self):
        #              https://aip.baidubce.com/rest/2.0/face/v3/detect
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        request_url = request_url + "?access_token=" + '24.d0de5125b5c456d4994888f7fb22cd87.2592000.1554561719.282335-15708099'

        params = {
            'image': self.get_img_base('./static/images/test.jpg'),
            'image_type': 'BASE64',
            'face_field': 'age,beauty,gender'
        }

        res = requests.post(request_url, data=params)
        result = res.text
        json_result = json.loads(result)
        code = json_result['error_code']
        gender = json_result['result']['face_list'][0]['gender']['type']
        beauty = json_result['result']['face_list'][0]['beauty']
        # print('以杨超越76.66的颜值为标准')
        # print(f'你的状态是:{code},你的性别是：{gender},你的颜值是：{beauty}')
        # print('通过AI识别，对于你的颜值人工智能给出的判定结果是：')
        if float(beauty) > 76.66:
            # print(f'哦！天啊，你居然比杨超越还美丽动人，颜值{beauty}分。')
            str1 = '哦！天啊，你居然比杨超越还美丽动人，颜值%s分。'%beauty
            return str1
            pass
        elif float(beauty) == 76.66:
            # print(f'不错哟，居然得分和杨超越一样')
            str2 = '不错哟，居然得分和杨超越一样'
            return str2
            pass
        else:
            # print(f'没关系，虽然{beauty}分，毕竟大家都是普通人')
            str3 = '没关系，虽然%s分，毕竟大家都是普通人'%beauty
            return str3
        pass

    def run(self):
        self.get_socre()

ai = AI()
ai.run()
