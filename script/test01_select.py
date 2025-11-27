import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)
from api.posts import PostsAPI

class TestSelect:
    def setup_method(self):
        self.test_api = PostsAPI()
        
    def test01_text_success(self):
        response = self.test_api.select_text(parameter="1")
        print(response.json())
        print("url为", response.url)
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        # assert '成功' in response.text
        # 断言json返回数据中title不为空
        assert len(response.json().get("title")) > 0