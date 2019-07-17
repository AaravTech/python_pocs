from fpdf import FPDF, HTMLMixin
from django.conf import settings

import datetime
import os
import math


class PDF_TOC(FPDF, HTMLMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._toc = []
        self._numbering = False
        self._numbering_footer = False
        self._num_page_no = 1

    def add_page(self, orientation='', format='', safe=False):
        super().add_page(orientation)
        if self._numbering:
            self._num_page_no += 1

    def start_page_nums(self):
        self._numbering = True
        self._numbering_footer = True

    def stop_page_nums(self):
        self._numbering = False

    def num_page_no(self):
        return self._num_page_no

    def TOC_entry(self, txt, level=0, link=None):
        self._toc.append({
            't': txt,
            'l': level,
            'p': self.num_page_no(),
            'link': link
        })

    def insert_TOC(self, location=1,
                   label_size=20,
                   entry_size=12,
                   tocfont='Arial',
                   label='Table of Contents'):

        self.stop_page_nums()
        self.add_page()
        tocstart = self.page

        self.set_font('Arial', 'B', label_size)
        self.set_fill_color(192, 192, 192)
        self.rect(1.5, 9.5, 7, 7, 'F')
        self.set_fill_color(237, 142, 60)
        self.rect(0, 8, 7, 7, 'F')
        self.cell(0, 5, label, 0, 1, 'L')
        self.ln(10)

        for item in self._toc:
            level = item['l']
            if level > 0:
                self.cell(level * 8)
            weight = ''
            # if level == 0:
            #     weight = 'B'
            txt = item['t']
            self.set_font(tocfont, weight, entry_size)
            strsize = self.get_string_width(txt)
            # self.write(self.font_size+2, txt, link=item['link'])
            self.cell(strsize+2, self.font_size+5, txt, link=item['link'])

            # Filling dots
            self.set_font(tocfont, '', entry_size)
            page_cell_size = self.get_string_width(str(item['p']))+2
            w = self.w - self.l_margin - self.r_margin - \
                page_cell_size - (level * 8) - (strsize + 2)
            nb = w/self.get_string_width('.')
            dots = '.' * (round(nb) - 1)
            self.cell(w, self.font_size+5, dots, 0, 0, 'R')

            # Page number
            self.cell(page_cell_size, self.font_size+5,
                      str(item['p']), 0, 1, 'R')

        # Grab it and move to selected location
        n = self.page
        n_toc = n - tocstart + 1
        last = []

        for i in range(tocstart, n+1):
            last.append(self.pages[i])

        # move pages
        for i in reversed(range(location - n_toc + 1, tocstart)):
            self.pages[i + n_toc] = self.pages[i]

        for i in range(n_toc):
            self.pages[location] = last[i]

    def footer(self):
        if not self._numbering_footer:
            return
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        self.cell(0, 7, str(self.num_page_no()), 0, 0, 'R')
        if not self._numbering:
            self._numbering_footer = False

    def _arc(self, x1, y1, x2, y2, x3, y3):
        h = self.h
        self._out('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} c '.format(
            x1*self.k, (h-y1)*self.k,
            x2*self.k, (h-y2)*self.k, x3*self.k, (h-y3)*self.k))

    def clipping_rounded_ect(self, x, y, w, h, r, outline=False):
        k = self.k
        hp = self.h
        op = 'S' if outline else 'n'
        MyArc = 4/3 * (math.sqrt(2) - 1)

        self._out('q {:.2f} {:.2f} m'.format((x+r) * k, (hp-y) * k))
        xc = x + w - r
        yc = y+r
        self._out('{:.2f} {:.2f} l'.format(xc * k, (hp-y) * k))
        self._arc(xc + r*MyArc, yc - r, xc + r, yc - r*MyArc, xc + r, yc)
        xc = x + w - r
        yc = y + h - r
        self._out('{:.2f} {:.2f} l'.format((x+w) * k, (hp-yc) * k))
        self._arc(xc + r, yc + r*MyArc, xc + r*MyArc, yc + r, xc, yc + r)
        xc = x + r
        yc = y + h - r
        self._out('{:.2f} {:.2f} l'.format(xc*k, (hp-(y+h)) * k))
        self._arc(xc - r*MyArc, yc + r, xc - r, yc + r*MyArc, xc - r, yc)
        xc = x + r
        yc = y + r
        self._out('{:.2f} {:.2f} l'.format((x) * k, (hp-yc)*k))
        self._arc(xc - r, yc - r*MyArc, xc - r*MyArc, yc - r, xc, yc - r)
        self._out(' W ' + op)

    def unset_clipping(self):
        self._out('Q')


class GenerateIPDataSheet(object):
    def __init__(self, obj=None):
        self.obj = obj
        self.img_dir = settings.BASE_DIR + '/ui/static/img/'

    def generate(self, filename=None):
        pdf = PDF_TOC('P', 'mm', 'A4')
        # pdf= PDF_TOC()
        pdf.set_font('Times', '', 12)
        pdf.add_page()
        # pdf.cell(0, 5, 'Cover', 0, 1, 'C')
        self.createCoverPage(pdf)

        items = [
            "Aviator",
            "Coresight SoC",
            "Cortex-A53",
            "Cortex-A72",
            "NIC400",
        ]
        for item in items:
            pdf.add_page()
            pdf.start_page_nums()
            link = pdf.add_link()
            self.createObjDetails(pdf, item)
            pdf.TOC_entry(item, 0, link)

        # Generate and insert TOC at page 2
        pdf.insert_TOC(2)
        if not filename:
            filename = 'ip_datasheet.pdf'
        pdf.output(filename, 'F')

    def createCoverPage(self, pdf):
        bg_image = self.img_dir + 'pdf_background.png'
        logo_image = self.img_dir + 'logos/designhub.png'
        pdf.image(bg_image, 0, 0, pdf.w, pdf.h)
        pdf.set_draw_color(134, 127, 186)        
        pdf.clipping_rounded_ect(
            pdf.w * 0.1, pdf.h * 0.33, pdf.w * 0.8, pdf.h * 0.33, 5, True)
        pdf.unset_clipping()
        pdf.set_text_color(255, 255, 255)
        pdf.image(logo_image, 10, 10, 51, 18)
        pdf.cell(35, 100, '', 0, 1, 'L')
        pdf.cell(35, 25, '', 0, 0, 'L')
        pdf.set_font('Arial', 'B', 25)
        pdf.cell(35, 25, 'IP: AVIATOR', 0, 1, 'L')
        pdf.set_draw_color(237, 142, 60)
        pdf.line(47, 130, 65, 130)
        pdf.line(47, 130.3, 65, 130.3)
        pdf.line(47, 130.6, 65, 130.6)
        pdf.cell(35, 25, '', 0, 0, 'L')
        pdf.set_font('Arial', '', 20)
        pdf.set_text_color(181, 202, 244)
        pdf.cell(50, 20, 'IP Revision: ', 0, 0, 'L')
        pdf.set_text_color(255, 255, 255)
        pdf.cell(35, 20, 'r1p0(Latest)', 0, 1, 'L')
        pdf.cell(35, 20, '', 0, 0, 'L')
        pdf.set_font('Arial', '', 20)
        pdf.set_text_color(181, 202, 244)
        pdf.cell(50, 20, 'Generated On: ', 0, 0, 'L')
        pdf.set_text_color(255, 255, 255)
        pdf.cell(35, 20, '05/03/2019 at 09:58 am', 0, 1, 'L')
        pdf.set_text_color(134, 127, 186)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(100, 100, '', 0, 1, 'L')
        pdf.cell(0, 1, '2019 ClioSoft®, Inc. All rights reserved.', 0, 1, 'C')

    def createObjDetails(self, pdf, item):
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(r=255, g=255, b=255)
        pdf.set_font('Arial', 'B', 20)
        pdf.cell(0, 5, item, 'L')
        pdf.ln()
        pdf.ln()
        pdf.set_font('Arial', 'B', 14)
        pdf.set_text_color(r=255, g=69, b=0)
        pdf.cell(0, 5, 'r1.0', 'L')
        pdf.ln()
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(0, 0, 0)
        desc = """
            <p><B>Hello This is demo description</B></p>
        """
        pdf.write_html(desc)
        header = ['Attribute Name', 'Attribute Value']
        data = [
            ["Technology", ""],
            ["Foundry", "Global Foundries"],
            ["Process", "40 mm"],
            ["Flows", "Synopsys"],
            ["Technology", ""],
            ["Foundry", "Global Foundries"],
            ["Process", "40 mm"],
            ["Flows", "Synopsys"],
            ["Technology", ""],
            ["Foundry", "Global Foundries"],
            ["Process", "40 mm"],
            ["Process", "40 mm"],
            ["Flows", "Synopsys"],
        ]
        pdf.ln()
        pdf.ln()
        self.data_table(pdf, header, data)

    def data_table(self, pdf, header, data):
        # Colors, line width and bold font
        pdf.set_fill_color(238, 239, 240)
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(238, 239, 240)
        pdf.set_line_width(.3)
        pdf.set_font('Arial', 'B', 12)
        # Header
        w = [pdf.w/2 - pdf.l_margin, pdf.w/2 - pdf.r_margin]
        for i in range(len(header)):
            pdf.cell(w[i], 12, " "*5 + header[i], 1, 0, 'L', True)
        pdf.ln()
        # Color and font restoration
        pdf.set_fill_color(252, 244, 234)
        pdf.set_text_color(0)
        pdf.set_font('')
        # Data
        fill = False
        for row in data:
            if row[1] == "":
                pdf.set_fill_color(252, 244, 234)
                pdf.cell(w[0], 10, " "*5 + row[0], 'LR', 0, 'L', True)
                pdf.cell(w[1], 10, " "*5 + row[1], 'LR', 0, 'L', True)
            else:
                pdf.set_fill_color(250, 250, 250)
                pdf.cell(w[0], 10, " "*5 + row[0], 'LR', 0, 'L', fill)
                pdf.cell(w[1], 10, " "*5 + row[1], 'LR', 0, 'L', fill)
                fill = not fill
            pdf.ln()
        # Closing line
        pdf.cell(sum(w), 0, '', 'T')


if __name__ == "__main__":
    ob = GenerateIPDataSheet()
    ob.generate()
