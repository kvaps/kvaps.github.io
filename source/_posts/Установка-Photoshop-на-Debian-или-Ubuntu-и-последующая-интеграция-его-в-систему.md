---
title: >-
  Установка Photoshop на Debian или Ubuntu и последующая интеграция его в
  систему
date: 2012-09-19 16:31:00
tags:
---

Сейчас я расскажу вам как установить Photoshop на debian или ubuntu, который будет вполне очень даже стабильно работать.  
О том как создать кнопку запуска, и как правильно установить последнюю версию wine под debian squeeze, debian wheezy или ubuntu.  
И о том как интегрировать Photoshop в систему, что бы открывались .PSD и другие файлы, непосредственно из самой системы.  
Всего за десять простых шагов:
<!-- more -->

И так, приступим:

## **Часть 1: Установка самого Photoshop'а**

  
**1\. Удаляем старые версии wine**
    
    
    sudo aptitude purge wine

  
**2\. Устанавливаем новый wine**

_Если ubuntu то:_
    
    
    sudo add-apt-repository ppa:ubuntu-wine/ppa  
     sudo apt-get update  
     sudo apt-get install wine1.5

  
_Если debian_
    
    
    ARCH=`uname -m | sed -e s/x86_64/amd64/ -e s/i.86/i386/`  
     wget -r -A "*_$ARCH.deb" http://dev.carbon-project.org/debian/wine-unstable/  
     sudo dpkg -i dev.carbon-project.org/debian/wine-unstable/*.deb  
     sudo apt-get install -f

  
**3\. Качаем winetricks и даем ему права на выполнение**
    
    
    wget http://winetricks.org/winetricks  
     chmod +x winetricks

  
_Проверим_
    
    
    ./winetricks

  
_Если у вас debian, winetricks скорее всего не запустится выдаст такую ошибку:_  
_  
_
    
    
    _wineserver not found_

_  
_  
_решение: укажем ему где у нас находится wineserver_
    
    
    sudo ln -s /usr/lib/wine-unstable/wineserver /usr/local/bin/wineserver

  
**4\. Начинаем установку нужных библиотек:**
    
    
    ./winetricks msxml3

  
_Жмем "Download now", качаем, устанавливаем._  
_Установим остальные, необходимые нам, библиотеки:_
    
    
    ./winetricks gdiplus msxml6 vcrun2005 vcrun2008 vcrun2010 atmlib ie6 fontsmooth-rgb allfonts

  
**5\. Качаем подходящий Photoshop упакованный в paf**  
**  
**  
_Сначала я скачал cs6, но там был какой-то баг с текстовыми полями. [[link]][1]_  
_Поэтому я скачал cs5.1 [[link]][2]_

**6\. Запускаем инсталлер и устанавливаем, я установил в Program Files**  
_(если директория не выберается, можно установить в другое место потом просто перенести куда хотим)_

Все теперь Photoshop установлен и нормально работает.

**7\. Что бы полноценно работать с хоткеями Photoshop'a, давайте перенаправим все "окно-управляющие" функции кнопки `<alt>` на кнопку `<win>`, и отключим меню окна по Alt+Click**
    
    
    gconftool-2 --set /apps/metacity/general/mouse_button_modifier --type string '<super>'  
    gconftool-2 --set /apps/metacity/window_keybindings/activate_window_menu --type string 'disabled'

&nbsp;

## **Часть 2: Инегрируем Photoshop в систему**

  
**8\. Сначала скачаем и установим иконку**
    
    
    wget http://upload.wikimedia.org/wikipedia/commons/5/58/Adobe_Photoshop_logo.svg  
     sudo mv Adobe_Photoshop_logo.svg /usr/share/app-install/icons/

  
**9\. Теперь создадим кнопку запуска и ассоциируем Photoshop с .PSD файлами**
    
    
    sudo nano ~/.local/share/applications/Photoshop.desktop

  
_с вот таким содержимым:_
    
    
    [Desktop Entry]  
     Type=Application  
     Name=Adobe Photoshop CS5  
     MimeType=image/psd;  
     Exec=env WINEPREFIX="/home/ИМЯ_ПОЛЬЗОВАТЕЛЯ/.wine" "/home/ИМЯ_ПОЛЬЗОВАТЕЛЯ/.wine/drive_c/Program Files/AdobePSPortable/PSD" %f  
     NoDisplay=false  
     StartupNotify=true  
     Icon=/usr/share/app-install/icons/Adobe_Photoshop_logo.svg  
     Categories=Graphics;

  
**10\. Ну и создадим небольшой скриптик который будет конвертировать нашим файлам имена и пути**
    
    
    nano "/home/ИМЯ_ПОЛЬЗОВАТЕЛЯ/.wine/drive_c/Program Files/AdobePSPortable/PSD"

  
_с таким содержимым:_
    
    
    #!/bin/sh  
     QUICKPARLOCATION="C:\Program Files\AdobePSPortable\AdobePSPortable.exe"  
     PARAM=`winepath -w "$*"`  
     wine "$QUICKPARLOCATION" "$PARAM"  
     exit 0

  
_сделаем его исполняемым_
    
    
    chmod +x "/home/ИМЯ_ПОЛЬЗОВАТЕЛЯ/.wine/drive_c/Program Files/AdobePSPortable/PSD"

Теперь все готово, Photoshop есть у нас в меню программ, и в диалоге "Открыть с помощью"

[1]: http://thepiratebay.se/torrent/7266185
[2]: http://thepiratebay.se/torrent/6908484/Adobe_Photoshop_CS5.1_Portable_Multilingual_%28PAF%29
