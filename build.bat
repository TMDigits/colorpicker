pyinstaller  --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --add-data "colorpicker\core\assets;colorpicker\core\assets" ^
    --hidden-import "pynput.keyboard._win32" ^
    --hidden-import "pynput.mouse._win32" ^
    --name colorpicker ^
    --icon "colorpicker\core\assets\icon.ico" ^
    colorpicker\__main__.py