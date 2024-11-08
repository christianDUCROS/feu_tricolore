from machine import Pin
import time

class Feu_Tricolore():
    '''
    A l'instanciation : saisir les numéros des broches
    
    Méthode  "allumer(couleur)" avec le paramètre 'rouge', 'vert' ou 'orange' pour affecter une couleur

    Méthode  "eteindre()  pour éteindre les 3 feux
   
    Méthode "clignoter(nb_fois,couleur, periode)" fait clignoter n fois  la couleur choisie avec une periode en ms

    Méthode "test()" permet d'allumer puis  eteindre toutes les feux pour valider les branchements
    '''
    def __init__(self, broche_rouge,broche_orange,broche_vert) :
        self.led_rouge = Pin(broche_rouge, Pin.OUT)    
        self.led_orange = Pin(broche_orange, Pin.OUT)    
        self.led_vert = Pin(broche_vert, Pin.OUT)   
        self.etat = ''
        
    def allumer(self,couleur):
        if couleur == 'rouge':   
            self.led_rouge.on()
            self.led_orange.off()
            self.led_vert.off()
            self.etat = 'rouge'
        elif couleur == 'orange':   
            self.led_rouge.off()
            self.led_orange.on()
            self.led_vert.off()
            self.etat = 'orange'
        elif couleur == 'vert':   
            self.led_rouge.off()
            self.led_orange.off()
            self.led_vert.on()
            self.etat = 'vert'
        else :
            self.led_rouge.off()
            self.led_orange.off()
            self.led_vert.off()
            self.etat = 'eteint'
        
    def eteindre(self) :
        self.led_rouge.off()
        self.led_orange.off()
        self.led_vert.off()
        self.etat = 'eteint'      
        
    def clignoter(self,n,couleur,periode):
        self.eteindre()
        time.sleep_ms(int(periode/2))
        for i in range(n) : 
            self.allumer(couleur) 
            time.sleep_ms(int(periode/2))
            self.eteindre()
            time.sleep_ms(int(periode/2))
        
    def test(self):
        print('debut test')
        self.led_rouge.on()
        self.led_orange.on()
        self.led_vert.on()
        time.sleep(5)
        self.led_rouge.off()
        self.led_orange.off()
        self.led_vert.off()
        print('fin de test')
        
if __name__ == '__main__':
    #instanciation
    feu1 = Feu_Tricolore(2,3,4)
    
    #méthodes
    feu1.test()
    
    feu1.allumer('rouge')
    print(feu1.etat)
    time.sleep(3)  # durée de l'état 
    
    feu1.eteindre()
    time.sleep(2)  # tempo
    feu1.clignoter(3, 'orange',1000) #3x - periode 1s
    