# Mall för paket, modul och testning

- **src** - Paket för källkoden.
- **test** - Testpaket för att testa olika aspekter av källkods- paketen och modulerna inklusive logik och funktionalitet.
- **main.py** - Huvudscript som importerar och exekverar relevanta procedurer som är definerade i källkoden.
- **\_\_init\_\_.py** - Obligatorisk kontruktorliknande konfigureringsmekanism för ett paket. Ett paket känns igen genom att ha en **\_\_init\_\_.py** fil lokaliserad i rotfoldern.

### Ordlista
- **Standardbibliotek** - Den samlade mängden definitioner och specifikationer som utgör grunden för ett programspråk.
- **Script** - Fil med körbar kod som typiskt endast är beroende av att ha tillgång till ett standardbibliotek via systemsökvägar, men i övrigt vara självständigt.
- **Modul** - Fil med körbar kod som är tänkt att vara en referens för andra moduler eller script som är lokaliserade någon annanstans.
- **Paket** - En folder som innehåller en samling av moduler och script som på olika sätt hör ihop. Ett paket kan även innehålla andra paket.
- **Bibliotek** - Samlingsord för alla paket, moduler och script som ingår i ett projekt. Biblioteket utgör typiskt sett hela källkoden för ett projekt.
- **Enhetstestning** - Ett enskilt test som syftar till att testa att någon logik eller sammanhängande funktionalitet är korrekt definerad i källkoden. Ett enhetstest ska gå snabbt att exekvera (typiskt mätt i  ms). Ett test som är beroende av mekanismer som är beroende av processer som ligger utanför det lokala projektet eller standardbilbioteket (exempelvis ett serveranrop) är tekniskt sett inte ett enhetstest.

### Överblick
![module_structure.png](https://gitlab.com/dareut/project_template/-/raw/master/notes/module_structure.png)
