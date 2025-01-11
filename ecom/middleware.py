# from django.shortcuts import redirect
# from django.http import HttpResponseRedirect
# from .models import HostingStatus

# # class HostingMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Check if HostingStatus exists and is inactive
# #         hosting_status = HostingStatus.objects.first()

# #         # Only redirect if hosting status exists, is inactive, and user is not already on the hosting-status page
# #         if hosting_status and not hosting_status.is_active:
# #             # Check if the user is not already on the hosting-status page
# #             if request.path != '/hosting-status/' and not request.path.startswith('/admin'):
# #                 return HttpResponseRedirect('/hosting-status/')  # Redirect to the hosting status page

# #         # Allow the request to pass through if conditions are not met
# #         return self.get_response(request)
