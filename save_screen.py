import time
from pathlib import Path
#保存当前界面截图
def test_savescreen(self):
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是"\"转义符
        pfilename = u'.\\image'
        pic_path = pfilename + '\\' + current_time1 + '_' + current_time + '.png'
        # 判断文件夹是否存在，不存在就新建一个新的
        if Path(pfilename).is_dir():
            pass
        else:
            Path(pfilename).mkdir()
        print(pic_path)
        self.driver.save_screenshot(pic_path)
