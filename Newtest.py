import winreg

path = winreg.HKEY_CURRENT_USER

software = winreg.OpenKeyEX(path, r"SOFTWARE\\")
new_key = winreg.CreateKey (software, "Kali")

winreg.SetvalueEX(new_key, "myvalue", 0, winreg.REG_SZ, "Hello World")
winreg.SetvalueEX(new_key, "myothervalue", 0, winreg.REG_SZ, "20")

if new_key:
    winreg.Closekey(new_key)