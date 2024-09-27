from django.test import TestCase
from app.models.work_requests import WorkRequest
from django.contrib.auth import get_user_model
from app.models.work_user_proposals import WorkUserProposal

User = get_user_model()


class WorkRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.work_request = WorkRequest.objects.create(
            title="Test Work Request",
            description="This is a test work request.",
            requester=self.user,
            status="pending",
            budget=100,
        )

    def test_work_request_creation(self):
        self.assertEqual(self.work_request.title, "Test Work Request")
        self.assertEqual(self.work_request.description, "This is a test work request.")
        self.assertEqual(self.work_request.requester.username, "testuser")
        self.assertEqual(self.work_request.status, "pending")
        self.assertIsNotNone(self.work_request.created_at)
        self.assertIsNotNone(self.work_request.updated_at)

    def test_work_request_str(self):
        self.assertEqual(str(self.work_request), "Test Work Request")


class WorkUserProposalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.work_request = WorkRequest.objects.create(
            title="Test Work Request",
            description="This is a test work request.",
            requester=self.user,
            budget=150,
            status="pending",
        )
        self.proposal = WorkUserProposal.objects.create(
            work_request=self.work_request,
            user=self.user,
            cost=45,
            proposal_text="This is a test proposal.",
        )

    def test_work_user_proposal_creation(self):
        self.assertEqual(self.proposal.work_request, self.work_request)
        self.assertEqual(self.proposal.user.username, "testuser")
        self.assertEqual(self.proposal.proposal_text, "This is a test proposal.")
        self.assertIsNotNone(self.proposal.created_at)
        self.assertIsNotNone(self.proposal.updated_at)

    def test_work_user_proposal_str(self):
        self.assertEqual(
            str(self.proposal), "Proposal by testuser for Test Work Request"
        )
