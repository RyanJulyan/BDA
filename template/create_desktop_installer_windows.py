
import os
import PyInstaller.__main__

# my spec file in "dev\config" dir
workdir = os.getcwd()
# fn_msi_spec = os.path.join(workdir, 'main_msi.spec')

# define the "dev\dist" and "dev\build" dirs
# os.chdir("..")
devdir = os.getcwd()
distdir = os.path.join(devdir, '../desktop_windows/dist')
builddir = os.path.join(devdir, '../desktop_windows/build')

# call pyinstaller directly
PyInstaller.__main__.run([
    'run_desktop.py',
    '--distpath', distdir,
    '--workpath', builddir,
    '--onefile',
    '--noconsole',
    '--windowed',
    '--clean',
    '--add-data', 'app;app',
    '--add-data', 'databases;databases',
    '--add-data', 'config.py;./',
    '--hidden-import', 'engineio.async_drivers',
    '--key', '1234567890123456',
    '--icon', './app/static/images/icon.ico',
    '--name', 'Flask BDA',
    ])