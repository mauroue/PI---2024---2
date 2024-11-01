from django.db import models
from app.models.work_requests import WorkRequest
from django.conf import settings


class WorkUserProposal(models.Model):
    work_request = models.ForeignKey(
        WorkRequest, on_delete=models.CASCADE, related_name="proposals"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proposal_text = models.TextField()
    cost = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Proposal by {self.user.username} for {self.work_request.title}"
