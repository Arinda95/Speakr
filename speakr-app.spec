# -*- mode: python -*-

block_cipher = None


a = Analysis(['speakr-app.py'],
             pathex=['C:\\Users\\Tony\\Desktop\\speakr\\SPEAKr'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='speakr-app',
          debug=False,
          strip=False,
          upx=True,
          console=False , version='version.txt', icon='icon.ico')
