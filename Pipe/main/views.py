from django.shortcuts import render, redirect, get_object_or_404
from .models import KeyMetrics
import csv

def index(request):
    message = None
    error = None

    if request.method == "POST":
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            error = "No file detected"
        elif not csv_file.name.endswith('.csv'):
            error = "File must have a .csv extension"
        else:
            # Read and decode the file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Check required columns
            required_columns = ['category', 'price', 'sale']  # Replace with your model fields
            if not all(col in reader.fieldnames for col in required_columns):
                error = f"CSV missing required columns: {', '.join(required_columns)}"
            else:
                # Save data to database
                row_count = 0
                for row in reader:
                    try:
                        KeyMetrics.objects.create(
                            category=row['category'],
                            price=float(row['price']),
                            sale=int(row['sale'])
                        )
                        row_count += 1
                    except ValueError:
                        # Skip invalid rows or log them
                        continue

                message = f"{csv_file.name} uploaded successfully with {row_count} rows."

    rows = KeyMetrics.objects.all()
    return render(request, 'main/index.html', {
        'message': message,
        'error': error,
        'rows': rows,
    })


def delete_metric(request, id):
    metric = get_object_or_404(KeyMetrics, id=id)
    metric.delete()
    return redirect('index')