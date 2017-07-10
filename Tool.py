# coding=UTF-8
#这里定义了一些工具类或者函数
from win32com.shell import shell
from win32com.shell import shellcon

#用于获取一些特定的路径
class Path:
	PERSONAL_DIR=shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_PERSONAL))