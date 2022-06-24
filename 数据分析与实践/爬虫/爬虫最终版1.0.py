import requests
import re
import json

headers = {'cookie': 'NTESSTUDYSI=6d7305fc04a84df1a282b643d555dc42; EDUWEBDEVICE=d8d507128fba4f5c89ebc1a8b678eff0; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1617709935; __yadk_uid=FFIpE2FmxtVIcx0cnUzSPaMcGWyu8F8S; WM_TID=uAINjV8s0%2BRBURBUARcvxYgqVTmaAG0B; WM_NI=wrR50VIEEswqEEyzJKAlvXPK4gMcYhNDDODtnfWphYqwjAklY13bZMUTtwT6UJPkX3SlY6F8XoQOZbcivUTJ3Jo%2FalREQVHSPY5VmUZ9UatcpVyzS0nfckjAAXcG33NhOWU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebab565879cabaef95095ac8fb3c85e878a8b84f43c8fe798a8c152b78b9fd3e12af0fea7c3b92ab5ae9ed6b35e8b9b8b94f67b879bb79bc94183b4bab9d341f8b98384dc648e9c8cb0c780aeba9991eb53b3a9a6a2ea689beffd83d947978cbc98d73e9796a08cdb3991b497d7c5349cb19fb0d96aa1b7bab6d742f196a1d0e468929b9fb7cb599487fbb7f05f9ae79b82f769b48ab79bd23caebaad8ce94b8388ada8b2398eb881b8d837e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1617882067'}
url = 'https://www.icourse163.org/university/view/all.htm#/'

uninames = list()    #列表存大学英文缩写
courses_id = list() #列表用以存一个学校的所有课程的ID

def get_school_name(url):
    "列表uninames中存放所有大学"
    resp = requests.get(url, headers = headers)
    resp.encoding = 'utf-8' #防止乱码
    uniname_1 = re.findall(r'<a class="u-usity f-fl" href="/university/(.*?)" target="_blank">',resp.text)
    return uniname_1


def get_school_id(uniname):
    "得到一个学校的id"
    url = 'https://www.icourse163.org/university/' + uniname + '#/c'
    resp = requests.get(url, headers = headers )
    resp.encoding = 'utf-8'
    school_id0 = re.findall(r'window.schoolId = "(\d+)";',resp.text)
    school_id = int(school_id0[0])
    return school_id


def get_course_id(school_id):
    "获取一个学校的所有慕课ID"
    courses_id_all = list() #第一页所有课程ID
    main_page_url = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=6d7305fc04a84df1a282b643d555dc42'
    data = {"schoolId":school_id,
            "p":1,
            "psize": 20,
            "type":1,
            "courseStatus":30 }
    resp = requests.post(url = main_page_url, headers = headers, data=data)
    resp.encoding = 'utf-8'
    courses_id_all += re.findall(r'.*?id.*?(\d+)',resp.text)      #一个学校的所有课程ID
    return courses_id_all


def store(data):
    "存储一个课程信息"
    file = open("result.json" , "a" , encoding="utf8")
    file.write(json.dumps(data, indent = 2, ensure_ascii = False))  #indent缩进2美观
    file.write("\n")
    file.write('\n')
    file.close()


def get_message(uniname):
    "遍历一个学校的所有课程信息，并调用store函数存储到result.json文件当中"
    for course_id in courses_id:
        course_url = "https://www.icourse163.org/course/" + uniname + "-" + course_id        
        resp = requests.get(url = course_url, headers = headers)
        resp.encoding = 'utf-8'       
        data = {}
        data['课程url'] = course_url
        data['课程名称'] = re.findall(r'window.courseDto[^n]+name:"([^"]+)"',resp.text)[0]
        data['开课大学'] = re.findall(r'window.schoolDto[^n]+name:"([^"]+)"',resp.text)[0]
        data['授课老师'] = re.findall(r'lectorName : "([^"]+)"',resp.text)
        course_times = re.findall(r'text : "开课时间不确定的学期"', resp.text)     # 1就是没开课
        if len(course_times) == 1:
            data['开课时间'] = "不确定"
            data['开课次数'] = 0
        else:
            course_times = re.findall( r'text : "([^-]+)-[^"]+"',  resp.text)
            data['开课时间'] = course_times[len(course_times)-1]
            data['开课次数'] = len(course_times)
        data['参加人数'] = int(re.findall(r'enrollCount : "([^"]+)"',resp.text)[0])
        store(data)
            

if __name__ == "__main__":
    print("已经开始爬了,在往result.json文件里存")
    url = ' https://www.icourse163.org/university/view/all.htm#/'
    uninames = get_school_name(url)
    for uniname in uninames:
        try:
            print("正在%s大学课程信息里面爬" % uniname)
            school_id = get_school_id(uniname)
            courses_id = get_course_id(school_id)
            get_message(uniname)
        except:                 
            continue
    print("爬完了!")