# Instalace pythonu
V našem kurzu budeme využívat nejnovější verzi pythonu 3.6 . Před začátkem kurzu by bylo dobré mít python nainstalovaný a mít ověřenou funkčnost. Níže je návod, jak jej nainstalovat a otestovat.

## Windows
### Stažení
Jdi na [stahovací stránku](https://www.python.org/downloads/) Pythonu a stáhni si instalátor nejnovější verze __Pythonu (3.6.0 a vyšší)__

Pokud máš novější počítač, nejspíš bude tvůj windows 64-bit, proto stáhni 64-bit verzi. Kdyby sis chtěl být jistý, koukni se do Systémových informací (__Start__ -> vyhledat "Systém" a otevřít "Systémové informace") a pod údajem o procesoru a RAM uvidíš tvůj typ operačního systému (32-bit nebo 64-bit).

### Instalace

Jedná se o normálni instalátor. Na začátku nezapomeň zaškrtnout "Add Python 3.6 to PATH" a zvol možnost "Install now", která zahrnuje editor IDLE, pip a dokumentaci.

![Alt Text](https://github.com/nguyeho7/vietcode2018/blob/master/tutorials/python_installation/python_installer.png "Python installer")


### Ověření funkčnosti
Spustíme program IDLE

![Alt Text](https://github.com/nguyeho7/vietcode2018/blob/master/tutorials/python_installation/IDLE.png "IDLE icon")

Otevře se okno Python Shell. Zkusíme napsat první příkaz:

```
print("Hello World!")
```

Python by nás měl pozdravit

![Alt Text](https://github.com/nguyeho7/vietcode2018/blob/master/tutorials/python_installation/python_shell_test.png "Hello World")

Pokud se podařilo, pak je instalace hotová

## macOS
### Stažení a instalace
Nejjednoduší bude si nainstalovat nástroj [Homebrew](https://brew.sh/index_cs), který řeší instalaci aplikací a knihoven. V příkazové řádce stačí zadat:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

a tím se nainstaluje  [Homebrew](https://brew.sh/index_cs).

Po instalaci stačí do příkazové řádky zadat:

```bash
$ brew install python3
```

### Ověření funkčnosti
V příkazové řádce pustíme:
```
python3
```

a v příkazové řádce by se mělo zobrazit něco podobného:

```
Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Zkusíme pozdravit svět následujícím příkazem:

```
print("Ahoj světe!")
```

a mělo by se objevit toto:

```
>>> print("Ahoj světe!")
Ahoj světe!
>>>
```
A tím jsme ověřili, že nám Python funguje.

## Linux
### Stažení a instalace
Na Linuxu python většinou bývá, zkontroluj příkazem:
```
$ python3 --version
```
Pokud se objeví "Python" a číslo verze (např. `Python 3.6.3`), máš nainstalováno

Pokud se objeví něco jako `bash: python3: command not found`, doinstaluješ Python následovně.
 - Fedora:
 ```
 $ sudo dnf install python3
 ```
 - Ubuntu:
 ```
 $ sudo apt-get install python3
 ```
Pokud máš starší verzi, updatuješ jej příkazy:

```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```

Pak přehodíme novou verzi místo staré:
```
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.6 /usr/bin/python3
```

### Ověření funkčnosti
V příkazové řádce pustíme:
```
python3
```

a v příkazové řádce by se mělo zobrazit něco podobného:

```
Python 3.6.3 (default, Oct 6 2017, 08:44:35)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Zkusíme pozdravit svět následujícím příkazem:

```
print("Ahoj světe!")
```

a mělo by se objevit toto:

```
>>> print("Ahoj světe!")
Ahoj světe!
>>>
```
A tím jsme ověřili, že nám Python funguje.
