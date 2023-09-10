from django.http import JsonResponse
import datetime
import pytz

def get_info(request):
    # Get query parameters from the URL
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track', 'backend')
    
    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')
    
    # Get current UTC time with validation
    utc_time = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Get GitHub URLs
    github_file_url = 'https://github.com/SamuelOshin/Zuri-endpoint-task/blob/main/task_one/views.py'
    github_repo_url = 'https://github.com/SamuelOshin/Zuri-endpoint-task.git'
    
    
    # Create the response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }
    
    return JsonResponse(response_data)
