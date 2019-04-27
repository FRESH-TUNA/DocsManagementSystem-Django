from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Document

# Create your views here.
def readDocument(request):
    documents = Document.objects.all()
    return render(request, 'DocsManageApp/index/index.html', {'documents':documents})

def createDocument(request):
    data = dict()
    if request.method == 'GET':
	    data['html_form'] = render_to_string('DocsManageApp/createDocumentPartial.html')
    else:
        form = DocumentForm(request.POST)
        if(form.is_valid()):
            form.save()
            documents = Document.objects.all()
            data['form_is_valid'] = True
            data['documents'] = render_to_string('DocsManageApp/readDocument.html',{'documents':documents})
            
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)
    
def updateDocument(request, pk):
    data = dict()
    document = get_object_or_404(Document,id=pk)

    if request.method == 'GET':    
        data['html_form'] = render_to_string('DocsManageApp/updateDocumentPartial.html', {'document':document}, request=request)
    else:
        form = DocumentForm(request.POST)
        if(form.is_valid()):
            form.save()
            documents = Document.objects.all()
            data['form_is_valid'] = True
            data['documents'] = render_to_string('DocsManageApp/readDocument.html',{'documents':documents})     
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)

def deleteDocument(request, pk):
    data = dict()
    document = get_object_or_404(Document,id=pk)

    if request.method == 'GET':
        data['html_form'] = render_to_string('DocsManageApp/deleteDocumentPartial.html', {'document':document} ,request=request)
    else:
        form = DocumentForm(request.POST)
        if(form.is_valid()):
            form.save()
            documents = Document.objects.all()
            data['form_is_valid'] = True
            data['documents'] = render_to_string('DocsManageApp/readDocument.html',{'documents':documents})
            
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)