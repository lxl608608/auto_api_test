import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)
from api.posts import PostsAPI

class TestPut:
    def setup_method(self):
        self.test_api = PostsAPI()
        
    def test03_text_success(self):
        data = {
            "userId": 1,
            "id": 10,
            "title": "哈哈哈",
            "body": "啊啊啊啊啊"
        }
        response = self.test_api.update_text(data=data, parameter="1")
        print(response.json())
        print("url为", response.url)
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        # assert '成功' in response.text
        # 断言json返回数据中code值
        # assert 200 == response.json().get("code")
        assert response.json()['title'] == data['title']