import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)
from api.posts import PostsAPI

class TestDelete:
    def setup_method(self):
        self.test_api = PostsAPI()
        
    def test04_text_success(self):
        data = {
            "userId": 1,
            "id": 101,
            "title": "哈哈哈",
            "body": "啊啊啊啊啊"
        }
        response = self.test_api.delete_text(parameter="1")
        print(response.json())
        print("url为", response.url)
        # 断言响应状态码
        assert 200 == response.status_code