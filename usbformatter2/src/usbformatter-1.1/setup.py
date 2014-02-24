from distutils.core import setup

setup(name='usbformatter',
      version='1.1',
      description='Pendrive formatting GUI utility.',
      author='Ronnie Andrew',
      author_email='ronnieandrew92@gmail.com',
      url='www.roandigital.com',
      #scripts=['usbformatter.py', 'usbformatter_ui.py'],
      data_files=[
          ('local/usbformatter/images', ['images/loading.gif', 'images/usb-usbformatter.png']),
          ('/usr/bin/', ['usbformatter']),
          ('/usr/share/icons/hicolor/256x256/apps/',['images/usb-usbformatter.png']),
          ('/usr/share/applications',['usbformatter.desktop']),
          ('local/usbformatter', ['usbformatter.py', 'usbformatter_ui.py']),
              ]
     )
