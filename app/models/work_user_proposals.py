from app import models
from app.models.users import User
from app.models.work_requests import WorkRequest


class WorkUserProposal(models.Model):
    work_request = models.ForeignKey(
        WorkRequest, on_delete=models.CASCADE, related_name="proposals"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Proposal by {self.user.username} for {self.work_request.title}"
