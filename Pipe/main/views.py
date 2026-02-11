from django.shortcuts import render
from .models import KeyMetrics
import csv

def index(request):
    message = None
    error = None

    if request.method == "POST":
        csv_file = request.FILES.get('csv_files')

        if not csv_file:
            error = "No file detected"
        elif not csv_file.name.endswith('.csv'):
            error = "File must have a .csv extension"
        else:
            # Read and decode the file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Check required columns
            required_columns = ['name', 'price', 'quantity']  # Replace with your model fields
            if not all(col in reader.fieldnames for col in required_columns):
                error = f"CSV missing required columns: {', '.join(required_columns)}"
            else:
                # Save data to database
                row_count = 0
                for row in reader:
                    try:
                        KeyMetrics.objects.create(
                            name=row['name'],
                            price=float(row['price']),
                            quantity=int(row['quantity'])
                        )
                        row_count += 1
                    except ValueError:
                        # Skip invalid rows or log them
                        continue

                message = f"{csv_file.name} uploaded successfully with {row_count} rows."

    return render(request, 'main/index.html', {
        'message': message,
        'error': error
    })
