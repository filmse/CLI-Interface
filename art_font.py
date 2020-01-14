from pyfiglet import Figlet

class ArtFont:

    def add_text(self):
        f = Figlet(font='slant')
        print(f.renderText('- Xenoptics -'))
        print('Welcome To Xenoptics Unit CLI')
