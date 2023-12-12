from django.shortcuts import render
from xhtml2pdf import pisa
from django.http import HttpResponse


# Create your views here.
from django import  forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class DTForm(forms.Form):
    your_email = forms.EmailField(max_length=200)
    date_input1 = forms.DateField(widget=AdminDateWidget())
    time_input1 = forms.DateField(widget=AdminTimeWidget())
    date_time_input1 = forms.DateField(widget=AdminSplitDateTime())
    date_input2 = forms.DateField(widget=AdminDateWidget())
    time_input2 = forms.DateField(widget=AdminTimeWidget())
    date_time_input2 = forms.DateField(widget=AdminSplitDateTime())


def generate_pdf_function(your_email,date_input1,time_input1, date_time_input1,date_input2,time_input2,date_time_input2):
  # Write your PDF generation code here
  html = '<html><body>'
  html += '<h1>Invoice</h1>'
  html += '<p>Your email: ' + your_email + '</p>'
  html += '<p>date_input1: ' + date_input1 + '</p>'
  html += '<p>time_input1: ' + time_input1 + '</p>'
  html += '<p>date_time_input1: ' + date_time_input1 + '</p>'
  html += '<p>date_input2: ' + date_input2 + '</p>'
  html += '<p>time_input2: ' + time_input2 + '</p>'
  html += '<p>date_time_input2: ' + date_time_input2 + '</p>'
  html += '</body></html>'
  result = pisa.CreatePDF(html, dest=BytesIO())
  return result

def generate_pdf(request):
      if request.method == 'POST':
       your_email = request.POST.get('your_email', '')
       date_input1 = request.POST.get('date_input1', '')
       time_input1 = request.POST.get('time_input1', '')
       date_time_input1 = request.POST.get('date_input1', '')
       date_input2 = request.POST.get('date_input2', '')
       time_input2 = request.POST.get('time_input2', '')
       date_time_input2 = request.POST.get('date_input2', '')
    # Generate PDF using xhtml2pdf
       result = generate_pdf_function(your_email,date_input1,time_input1, date_time_input1,date_input2,time_input2,date_time_input2)
      if result.err:
       return HttpResponse('Error generating PDF: %s' % result.err)
       response = HttpResponse(content_type='application/pdf')
       response.write(result.dest.getvalue())
       return response
       return render(request, 'index.html')