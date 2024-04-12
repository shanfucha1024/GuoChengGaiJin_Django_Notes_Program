from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
# 冒烟测试

# 第一次修改
# from django.test import TestCase

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

# Create your tests here.

# 第二次修改
# from django.test import TestCase
# from django.urls import resolve
# from lists.views import home_page

# class HomePageTest(TestCase):
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)


# 第三次修改
# class HomePageTest(TestCase):
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)
#     def test_home_page_return_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode('utf-8')
#         self.assertTrue(html.startswith('<html>'))
#         self.assertIn('<title>To-Do lists</title>',html)
#         self.assertTrue(html.endswith('</html>'))


#第四次修改
class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    # # def test_home_page_return_correct_html(self):
    # #     response = self.client.get('/')
    # #     self.assertTemplateUsed(response, 'home.html')
    # def test_uses_home_template(self):
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response,'home.html')
    # def test_can_save_a_POST_request(self):
    #     response = self.client.post('/',data={'item_text': 'A new list item'})
    #     self.assertIn('A new list item', response.content.decode())
    #     self.assertTemplateUsed(response, 'home.html')
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

