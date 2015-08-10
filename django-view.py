def post_form_upload(request):
    if request.method == 'GET':
        form = MyForm()
        template_name = 'myform.html'
        return render(request, template_name, {'form': form,})
    else:
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():

            id=form.cleaned_data['id']
            user = request.user
            if id:
                w = get_object_or_404(MyModel, pk=id)
                if w.user != request.user:
                    return HttpResponseForbidden()
            else:
                w = MyModel()
                w.id=None

            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = ''

            if 'document' in request.FILES:
                document = request.FILES['document']
            else:
                document = ''


            if(form.cleaned_data['image_changed']):
                if(form.cleaned_data['image_data']):
                    # drag and drop
                    image_url = "/plus.png"
                    image_data = form.cleaned_data['image_data']
                    processed_image_data = base64.b64decode(image_data.split(",",1)[1])
                    lf = tempfile.NamedTemporaryFile()
                    lf.write(processed_image_data)
                    imagea=files.File(lf)
                    imageafn=image_url.split("/")[-1]
                    w.image.save(imageafn,imagea, save=False)
                elif(form.cleaned_data['previous_image']):
                    # Changed by button
                    image_url = form.cleaned_data['previous_image']
                    requestimage = requests.get(image_url, stream=True)
                    lf = tempfile.NamedTemporaryFile()
                    for block in requestimage.iter_content(1024 * 8):
                        if not block:
                            break
                        lf.write(block)
                    imagea=files.File(lf)
                    imageafn=image_url.split("/")[-1]
                    w.image.save(imageafn,imagea, save=False)
                else:
                    # upload
                    w.image = image


            if(form.cleaned_data['document_changed']):
                if(form.cleaned_data['document_data']):
                    # drag and drop
                    image_url = "/plus.png"
                    image_data = form.cleaned_data['document_data']
                    processed_image_data = base64.b64decode(image_data.split(",",1)[1])
                    lf = tempfile.NamedTemporaryFile()
                    lf.write(processed_image_data)
                    imagea=files.File(lf)
                    imageafn=image_url.split("/")[-1]
                    w.document.save(imageafn,imagea, save=False)
                else:
                    w.document=document
            w.save()
            return HttpResponseRedirect("/")
        else:
            print (form.errors)
            return HttpResponseRedirect("/fail")
