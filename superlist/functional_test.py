from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import unittest

# servico = Service(ChromeDriverManager().install())
# browser = webdriver.Chrome(service=servico)
#
# browser.get('http://localhost:8000')
# sleep(10)
#
# assert 'To-Do' in browser.title
#
# browser.quit()


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.servico = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.servico)


    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online insteressante
        # para lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam
        # lista de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Ele é convidade a inserir um item de  tarefa imediatamente


if __name__ == '__main__':
    unittest.main(warnings='ignore')
