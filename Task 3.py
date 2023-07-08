def submit_exam(request):
    if request.method == 'POST':
        # Retrieve the selected choices from the form data
        selected_choices = request.POST.getlist('choice')
        
        # Process the selected choices and store the relevant information in your database
        # You might need to associate the choices with a specific user or exam instance
        
        # Redirect to the exam result page or any other appropriate page
        return redirect('exam_result')
    else:
        # Handle the case when the request method is not POST, e.g., display the exam form
        # Retrieve the relevant exam and question data from your models
        
        return render(request, 'exam_submission.html', {'questions': questions})
