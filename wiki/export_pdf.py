import markdown
import pdfkit
import smtplib
from email.mime.text import MIMEText

class export_pdf(object):
    def return_pdf(self, page):
        html_text = markdown.markdown(page.html, output_format='html4')

        path_wkthmltopdf = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        options = {'--header-html': r'C:\Users\zv\PycharmProjects\Riki\wiki\web\templates\header.html'}
        pdf = pdfkit.from_string(html_text, False, options=options, configuration=config)
        print "test 2"
        return pdf

    def mail_pdf(self, page, address):
        pdf = self.return_pdf(page)
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.login("bestwikiteam@gmail.com", "Software440")
        msg = " \n  Hello!"
        server.sendmail("bestwikiteam@gmail.com", address, msg)





if __name__ == '__main__':
    inst = export_pdf()
    inst.return_pdf()