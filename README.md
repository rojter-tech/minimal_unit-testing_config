# Mall för paket, modul och testning

## Projektets organisering
```
├── src                           <- Källkodspaketet, vanlig förkortning för "source".
     ├── utilities                <- Ett "paket i paketet", kan vara ett bra upplägg om man har 
                                     väldigt mycket kod som ska hållas isär med övrig källkod.
         ├── __init__.py          <- För att konfigurera "utilities". Detta är nödvändigt för att göra 
                                     paketet helt självständigt.
         ├── __main__.py          <- Om man vill exekvera något särskilt när man kör "utilities" direkt.

         └── useful_functions.py  <- Modulen för paketet utilities.
     ├── __init__.py              <- För att konfigurera "src". Detta är nödvändigt för att göra 
                                     paketet helt självständigt.
     └── __main__.py              <- Om man vill exekvera något särskilt när man kör "src" direkt.
├── test                          <- Testpaketet, namnet "test" är default för att unittest ska
                                     hitta testmodulerna som defineras här inne.
     ├── __init__.py              <- Koden här körs obligatoriskt varje gång test importeras eller körs.
                                     Särkilt när enhetstester ska genomföras.
     └── test_import.py           <- Testmodul för att köra enhetstester relaterade till logik i källkoden. 
                                     Prefixet "test_" används för att unittest ska förstå vad som är en
                                     testmodul.
                                     Även andra så kallade hjälpmoduler kan skapas i test om man så 
                                     önskar. En modul är alltid en fil. Ett paket är alltid en mapp.
```

- **src** - Paket för källkoden.
- **src/utilities** - Ytterligare ett paket i paketet src.
- **test** - Testpaket för att testa olika aspekter av källkods- paketen och modulerna inklusive logik och funktionalitet.
- **external_main.py** - Huvudskript som importerar och exekverar relevanta procedurer som är definerade i källkoden externt.
- **\_\_init\_\_.py** - Obligatorisk kontruktorliknande konfigureringsmekanism för att "initiera" ett paket. Ett paket känns igen genom att ha en **\_\_init\_\_.py** fil lokaliserad i rotfoldern. Typisk användning av **\_\_init\_\_.py** är att importera referenser som är nödvändiga eller önskvärda. Alla referenser som importeras i **\_\_init\_\_.py** importeras automatiskt när paketet självt importeras.
- **\_\_main\_\_.py** - Valbar exeveringsmekanism för att kunna "köra ett paket". Typiskt handlar det om inledande standardrutiner som alltid är tänkt att köras vid "uppstart" av en exekveringskedja som typiskt utgör ett självständigt program. Exempelvis kan det röra sig om att leda användaren till en användarmeny som skulle kunna vara en del av de standardrutiner som alltid körs när ett program startas.

### Ordlista
- **Standardbibliotek** - Den samlade mängden definitioner och specifikationer som utgör grunden för ett programspråk.
- **Skript** - Fil med körbar kod som typiskt endast är beroende av att ha tillgång till ett standardbibliotek via systemsökvägar, men i övrigt vara självständigt.
- **Modul** - Fil med körbar kod som är tänkt att vara en referens för andra moduler eller skript som är lokaliserade någon annanstans.
- **Paket** - En folder som innehåller en samling av moduler och skript som på olika sätt hör ihop, som faktiskt referens eller konceptuellt. Ett paket kan även innehålla andra paket.
- **Bibliotek** - Samlingsord för alla paket, moduler och skript som ingår i ett eller flera projekt. Biblioteket utgör typiskt sett hela källkoden för ett projekt.
- **Enhetstestning** - Ett enskilt test som syftar till att testa att någon logik eller sammanhängande funktionalitet är korrekt definerad i källkoden. Ett enhetstest ska gå snabbt att exekvera (typiskt mätt i  ms). Ett test som är beroende av mekanismer och processer som ligger utanför det lokala projektet eller standardbilbioteket (exempelvis ett serveranrop) är tekniskt sett inte ett enhetstest.

### Överblick
![module_structure.png](https://gitlab.com/dareut/project_template/-/raw/master/notes/module_structure.png)
