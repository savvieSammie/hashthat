from django.test import TestCase
from django.core.exceptions import ValidationError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .forms import HashForm
import hashlib
from .models import Hash




class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')  
        self.assertIn('Enter hash here:', self.browser.page_source)

    
    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000') 
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()
        self.assertIn('cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676', self.browser.page_source)


    def tearDown(self):
        self.browser.quit()



class UnitTest(TestCase):
    def test_homepage_template(self):
        reponse = self.client.get('')
        self.assertTemplateUsed(reponse, 'hashing/home.html')


    def test_home_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertTrue('cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676', text_hash)

    def saveHash(self): 
        #create a hash object and save it
        hash = Hash()
        hash.text = 'hello'
        hash.hash = 'cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676'
        hash.save()
        return hash

    def test_hash_object(self):
        hash = self.saveHash()
        pulled_hash = Hash.objects.get(hash='cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676')
        self.assertEqual(hash.text, pulled_hash.text)

    def test_viewing_hash(self):
        #create a hash object and save it
        hash = self.saveHash()
        response = self.client.get('/hash/cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676')
        self.assertContains(response, 'hello')

    def test_bad_data(self):
        def badHash()
            hash = Hash()
            hash.hash = 'cd2eca3535741f27a8ae40c31b0c41d4057a7a7b912b33b9aed86485d1c84676aaaaaaaa'
            hash.full_clean()
        self.assertRaises(ValidationError, badHash)    








