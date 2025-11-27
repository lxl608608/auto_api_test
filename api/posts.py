import requests
import config

class PostsAPI:
    # 初始化
    def __init__(self):
        # 查询--get
        self.url_select_user_all_text = config.BASE_URL + "posts/1/comments"
        self.url_select_user_one_text = config.BASE_URL + "comments?postId=1"
        # 上传-post  查询-get  删除-delete  查询-get  修改-put patch-上传修改的部分就可以
        self.url_all_text = config.BASE_URL + "posts"
        
    # 查询
    def select_text(self, parameter):
        return requests.get(url=self.url_all_text + f"/{parameter}")
    
    # 添加
    def add_text(self, data):
        return requests.post(url=self.url_all_text, json=data)
    
    # 修改
    def update_text(self, parameter, data):
        return requests.put(url=self.url_all_text + f"/{parameter}", json=data)
    
    # 删除
    def delete_text(self, parameter):
        return requests.delete(url=self.url_all_text + f"/{parameter}")
    