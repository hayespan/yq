#!/usr/bin/env python

from PIL import Image
 
color = 'MNHQ$OC?7>!:-;.'
 
def to_html(func):
    html_head = '''
            <html>
              <head>
                <style type="text/css">
                  body {font-family:Monospace; font-size:5px;}
                </style>
              </head>
            <body> '''
    html_tail = '</body></html>'
 
    def wrapper(img):
        pic_str = func(img)
        pic_str = ''.join(l + ' <br/>' for l in pic_str.splitlines())
        return html_head + pic_str + html_tail
 
    return wrapper


def make_char_img(img):
    pix = img.load()
    pic_str = ''
    width, height = img.size
    for h in xrange(height):
        for w in xrange(width):
            pic_str += color[int(pix[w, h]) * 14 / 255]*2
        pic_str += '\n'
    return pic_str
 

def preprocess(img_name):
    img = Image.open(img_name)
 
    w, h = img.size
    #m = max(img.size)
    m = w
    delta = m / 50.0
    print w, h, delta
    w, h = int(w / delta), int(h / delta)
    img = img.resize((w, h))
    img = img.convert('L')
 
    return img
 
def save_to_file(filename, pic_str):
    outfile = open(filename, 'w')
    outfile.write(pic_str)
    outfile.close()
 
def main():
    img = preprocess('2')

    pic_str = to_html(make_char_img)(img)
    save_to_file('char.html', pic_str)

    txt_str = make_char_img(img)
    save_to_file('char.txt', txt_str)
 
if __name__ == '__main__':
    main()
