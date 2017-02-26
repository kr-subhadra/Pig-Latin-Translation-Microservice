from django.test import TestCase
import unittest
from PigLatin import *

class TestBasic(unittest.TestCase):
    def test_basic_1(self):
        a = convert_sentence('Pig, banana, trash, happy! duck 5 glove. Eat omelet are')
        self.assertEqual('Igpay, ananabay, ashtray, appyhay! uckday 5 oveglay. Eatyay omeletyay areyay', a)
    
    def test_basic_2(self):
        b = convert_sentence('There once was a farmer named John. He had 3 cats.')
        self.assertEqual('Erethay onceyay asway ayay armerfay amednay Ohnjay. Ehay adhay 3 atscay.', b)
    
    def test_basic_3(self):
        c = convert_sentence('This also seems like a good time to explicitly say that all of your test classes and files should start with test! If not, they will not be run! If you have a test not running and everything else looks right, this is probably your problem. Also note that they cannot be named the same thing! These will overwrite one another with the last one being imported into the file running. It is generally a good practice to name your tests something that is certain to be unique. I generally tend to follow whatever naming convention I’ve used for my named url patterns.')
        self.assertEqual('Isthay alsoyay eemssay ikelay ayay oodgay imetay otay explicitlyyay aysay atthay allyay ofyay ouryay esttay assesclay andyay ilesfay ouldshay artstay ithway esttay! Ifyay otnay, eythay illway otnay ebay unray! Ifyay ouyay avehay ayay esttay otnay unningray andyay everythingyay elseyay ookslay ightray, isthay isyay obablypray ouryay oblempray. Alsoyay otenay atthay eythay annotcay ebay amednay ethay amesay ingthay! Esethay illway overwriteyay oneyay anotheryay ithway ethay astlay oneyay eingbay importedyay intoyay ethay ilefay unningray. Ityay isyay enerallygay ayay oodgay acticepray otay amenay ouryay eststay omethingsay atthay isyay ertaincay otay ebay uniqueyay. Iyay enerallygay endtay otay ollowfay ateverwhay amingnay onventioncay I’veyay usedyay orfay myay amednay urlyay atternspay.', c)

    def test_basic_4(self):
        d = convert_sentence('I am honest!')
        self.assertEqual('Iyay amyay honestyay!', d)
    
    def test_basic_5(self):
        e = convert_sentence('xray igloo object under koala yellow ggg queen square equal? therapy yttria')
        self.assertEqual('xrayyay iglooyay objectyay underyay oalakay ellowyay gggay ueenqay uaresqay equalyay? erapythay iayttray', e)

if __name__ == '__main__':
        unittest.main()
