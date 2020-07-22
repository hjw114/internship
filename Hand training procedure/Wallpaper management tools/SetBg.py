#coding=gbk
import win32api, win32con, win32gui

def set_wallpaper(img_path):
    # ��ָ��ע���·��
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # ���Ĳ���:2����,0����,6��Ӧ,10���,0ƽ��
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # ���Ĳ���:1��ʾƽ��,������еȶ���0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # ˢ������
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
