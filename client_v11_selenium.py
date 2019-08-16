# _*_coding : UTF-8_*_
# 开发团队：NONE
# 开发人员：41570
# 开发时间：2019/7/14 8:55
# 文件名称：client_v1.PY
# 开发工具：PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_words(driver):
    word_list = []
    pron_list = []
    chin_list = []
    a_list1 = driver.find_elements_by_xpath("//div[@class='dojoxGridContent']//div[@role='presentation']//\
    td[@tabindex='-1' and @role='gridcell']")

    for i in range(len(a_list1)):
        if i in range(1, len(a_list1), 4):
            word_list.append(a_list1[i].text)
        elif i in range(2, len(a_list1), 4):
            pron_list.append(a_list1[i].text)
        elif i in range(3, len(a_list1), 4):
            chin_list.append(a_list1[i].text)

    for i in range(len(word_list)):
        dict[word_list[i]] = [pron_list[i], chin_list[i]]


if __name__ == '__main__':
    url = 'http://www.wordmemo.com/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.get(url)
    dropdown = driver.find_element_by_xpath("//div[@class='btn-group pull-right']")
    dropdown.click()
    user = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    button = driver.find_element_by_id("login")
    time.sleep(1)
    user.send_keys("wangjh100231")
    time.sleep(1)
    password.send_keys("100231")
    time.sleep(2)
    button.click()
    time.sleep(4)
    chuguo = driver.find_element_by_id("dijit__TreeNode_6")
    chuguo.click()
    time.sleep(1)
    ielts = driver.find_element_by_id("dijit__TreeNode_16")
    ielts.click()
    time.sleep(1.5)
    # 雅思核心词汇3497
    core = driver.find_element_by_id("dijit__TreeNode_20")
    core.click()
    # 雅思考试词汇必备7971个
    # total = driver.find_element_by_id("dijit__TreeNode_21")
    # total.click()
    time.sleep(1)
    brower = driver.find_element_by_xpath("//span[@widgetid='memoDlg_browseBtn']")
    brower.click()
    time.sleep(4)
    dict = {}
    count = 0

    str = driver.find_element_by_xpath("//div[@aria-labelledby='dijit_Dialog_0_title']//div[@data-dojo-attach-point=\
    'containerNode']//div[@class='dijitTreeNode dijitTreeNodeUNCHECKED dijitUNCHECKED dijitTreeIsRoot']").get_attribute("id")
    print(type(str))
    print(str)
    li = str.split("_")
    print(li)
    print(type(li[3]))
    n = eval(li[3]) + 1

    for i in range(n, n+26):
        a = driver.find_element_by_id("dijit__TreeNode_{}".format(i))
        a.click()
        time.sleep(3)
        b = driver.find_element_by_xpath("//div[@title='首页']")
        b.click()
        time.sleep(3)
        get_words(driver)
        time.sleep(3)

        while driver.find_element_by_xpath("//div[@title='下一页']").get_attribute('tabindex') == '-2':
            next_page = driver.find_element_by_xpath("//div[@title='下一页']")
            next_page.click()
            time.sleep(3)
            get_words(driver)
            count += 1
            print(count)

    print(len(dict))

    with open("ielts_dict_core.txt", "a+", encoding="utf-8") as f:
        for k in dict:
            f.write(k + ":" + str(dict[k]) + "\n")
        f.write("一共收录{}个单词".format(len(dict)))



