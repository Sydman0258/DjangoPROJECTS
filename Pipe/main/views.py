from django.shortcuts import render

def index(request):
    message=None
    error = None

    if request.method=="POST":
        csv_file=request.FILES.get('csv_files')


        if not csv_file:
            error="No files detected"
        elif not csv_file.name.endswith('.csv'):
            error="Need .csv extension"
        else:
            message=f"{csv_file.name} uploaded successfully"
    
    return render(request,'main/index.html',{
        'message':message,
        'error':error
    })