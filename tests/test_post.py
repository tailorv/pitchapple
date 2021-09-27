import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Maxwell = User(full_name = "Maxwell Munene",
                                username = "maxwell_m",
                                password = "easy",
                                email = "maxwell@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hallo Welt! Ich bin hier",
                            user_id = self.user_Maxwell.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.post_id,
                                    user_id = self.user_Maxwell.id)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Maxwell, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))