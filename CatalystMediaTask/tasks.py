import csv
import time
import pandas as pd
from celery import shared_task
from company.models import Company, UploadedFile
from company.ws_client import send_message_view

@shared_task
def load_my_file(file_id, client_id):
    new_catalyst = UploadedFile.objects.get(id=file_id)
    dataset = new_catalyst.file.read().decode('utf-8').splitlines()
    print("load start")
    reader = csv.DictReader(dataset)
    rows = list(reader)  # Convert the reader to a list to count the rows
    total_size = len(rows)
    
    # Calculate the chunk size
    chunk_size = total_size // 100 if total_size > 100 else 1  # Maximum of 100 chunks

    completed_chunks = 0
    
    # Process the list in chunks
    for i in range(0, total_size, chunk_size):
        # Get the current chunk of data
        chunk = rows[i:i + chunk_size]
        
        # Update or create records for each row in the current chunk
        try:
            df = pd.DataFrame(chunk)
            df.drop('', axis=1, inplace=True)
            df.rename(columns={
                                'name':'name',
                                'domain': 'domain',
                                'year founded': 'year_founded',
                                'industry': 'industry',
                                'locality': 'locality',
                                'country': 'country',
                                'linkedin url': 'linkedin_url',
                                'current employee estimate': 'employees_from',
                                'total employee estimate': 'employees_to',
                                }, inplace=True)
            df = df[["name", "domain", "year_founded", "industry", "locality", "country", "linkedin_url", "employees_from", "employees_to"]]
            # df.drop_duplicates(keep='first')
            data_final = df.to_dict('records')
            data_objs = [Company(**x) for x in data_final]
            Company.objects.bulk_create(data_objs)
        except Exception as ex:
            print("oo")

        completed_chunks += len(chunk)
        
        # Calculate and print completion percentage
        percentage = (completed_chunks / total_size) * 100
        print(f"Loading... {percentage:.2f}% completed")
        send_message_view(client_id, percentage)  
    if new_catalyst.file:
        new_catalyst.file.delete(save=False)
    new_catalyst.delete()
