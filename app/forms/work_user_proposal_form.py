from django import forms
from app.models.work_user_proposals import WorkUserProposal


class WorkUserProposalForm(forms.ModelForm):
    class Meta:
        model = WorkUserProposal
        fields = ["proposal_text", "cost"]
        widgets = {
            "proposal_text": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Enter your proposal here"}
            ),
            "cost": forms.NumberInput(
                attrs={"min": 0, "step": 1, "placeholder": "Enter cost in cents"}
            ),
        }
        labels = {"proposal_text": "Proposal", "cost": "Cost (in cents)"}

    def clean_cost(self):
        cost = self.cleaned_data["cost"]
        if cost < 0:
            raise forms.ValidationError("Preço não pode ser negativo.")
        return cost

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["proposal_text"].required = True
        self.fields["cost"].required = True
