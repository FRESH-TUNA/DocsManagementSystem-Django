from django.shortcuts import render
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
        form = DocumentForm(instance=document)
	    data['html_form'] = render_to_string('DocsManageApp/updateDocumentPartial.html', {'document':document})
    else:
        form = DocumentForm(request.POST)
        if(form.is_valid()):
            form.save()
            documents = Document.objects.all()
            data['form_is_valid'] = True
            data['documents'] = render_to_string('DocsManageApp/readDocument.html',{'documents':document})     
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)

def deleteDocument(request, pk):
    data = dict()
    if request.method == 'GET':
	    data['html_form'] = render_to_string('DocsManageApp/deleteDocumentPartial.html')
    else:
        form = DocumentForm(request.POST)
        if(form.is_valid()):
            form.save()
            documents = Document.objects.all()
            data['form_is_valid'] = True
            data['documents'] = render_to_string('DocsManageApp/readDocument.html',{'documents':document})
            
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)