# Mall för paket, modul och testning

- **src** - Paket för källkoden.
- **test** - Testpaket för att testa olika aspekter av källkods- paketen och modulerna inklusive logik och funktionalitet.
- **main.py** - Huvudscript som importerar och exekverar relevanta procedurer som är definerade i källkoden.
- **\_\_init\_\_.py** - Obligatorisk kontruktorliknande konfigureringsmekanism för att "initiera" ett paket. Ett paket känns igen genom att ha en **\_\_init\_\_.py** fil lokaliserad i rotfoldern. Typisk användning av **\_\_init\_\_.py** är att importera referenser som är nödvändiga eller önskvärda. Alla referenser som importeras i **\_\_init\_\_.py** importeras automatiskt när paketet självt importeras.
- **\_\_main\_\_.py** - Valbar exeveringsmekanism för att kunna "köra ett paket". Typiskt handlar det om inledande standardrutiner som alltid är tänkt att köras vid "uppstart" av en exekveringskedja som typiskt utgör ett självständigt program. Exempelvis kan det röra sig om att leda användaren till en användarmeny som skulle kunna vara en del av de standardrutiner som alltid körs när ett program startas.

### Ordlista
- **Standardbibliotek** - Den samlade mängden definitioner och specifikationer som utgör grunden för ett programspråk.
- **Script** - Fil med körbar kod som typiskt endast är beroende av att ha tillgång till ett standardbibliotek via systemsökvägar, men i övrigt vara självständigt.
- **Modul** - Fil med körbar kod som är tänkt att vara en referens för andra moduler eller script som är lokaliserade någon annanstans.
- **Paket** - En folder som innehåller en samling av moduler och script som på olika sätt hör ihop. Ett paket kan även innehålla andra paket.
- **Bibliotek** - Samlingsord för alla paket, moduler och script som ingår i ett projekt. Biblioteket utgör typiskt sett hela källkoden för ett projekt.
- **Enhetstestning** - Ett enskilt test som syftar till att testa att någon logik eller sammanhängande funktionalitet är korrekt definerad i källkoden. Ett enhetstest ska gå snabbt att exekvera (typiskt mätt i  ms). Ett test som är beroende av mekanismer och processer som ligger utanför det lokala projektet eller standardbilbioteket (exempelvis ett serveranrop) är tekniskt sett inte ett enhetstest.

### Överblick
![module_structure.png](https://gitlab.com/dareut/project_template/-/raw/master/notes/module_structure.png)
