from django import forms
from app.models.work_user_proposals import WorkUserProposal


class WorkUserProposalForm(forms.ModelForm):
    class Meta:
        model = WorkUserProposal
        fields = ["proposal_text", "cost"]
        widgets = {
            "proposal_text": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Digite sua proposta aqui"}
            ),
            "cost": forms.NumberInput(
                attrs={"min": 0, "step": 1, "placeholder": "Digite o custo em centavos"}
            ),
        }
        labels = {"proposal_text": "Proposta", "cost": "Custo (em centavos)"}

    def clean_cost(self):
        cost = self.cleaned_data["cost"]
        if cost < 0:
            raise forms.ValidationError("O custo não pode ser negativo.")
        return cost

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["proposal_text"].required = True
        self.fields["cost"].required = True
