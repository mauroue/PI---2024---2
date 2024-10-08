document.addEventListener('DOMContentLoaded', function() {
  var actionModal = document.getElementById('actionModal');
  actionModal.addEventListener('show.bs.modal', function(event) {
    var button = event.relatedTarget;
    var action = button.getAttribute('data-action');
    var workRequestId = button.getAttribute('data-work-request-id');

    var form = document.getElementById('actionForm')
    var modalLabel = document.getElementById('actionModalLabel');
    var modalMessage = document.getElementById('modalMessage');
    var confirmButton = document.getElementById('confirmButton');

    if (action === 'cancel') {
      modalLabel.textContent = 'Cancelar';
      modalMessage.textContent = 'Você tem certeza de que deseja cancelar esta solicitação de trabalho?';
      form.action = '/work_requests/' + workRequestId + '/cancel/';
      confirmButton.textContent = 'Sim, Cancelar';
    } else if (action === 'apply') {
      modalLabel.textContent = 'Aplicar';
      modalMessage.textContent = 'Você tem certeza de que deseja se candidatar a esta solicitação de trabalho?';
      form.action = '/work_requests/' + workRequestId + '/apply/';
      confirmButton.textContent = 'Sim, Aplicar';
    } else if (action === 'logout') {
      modalLabel.textContent = 'Sair';
      modalMessage.textContent = 'Você tem certeza de que deseja sair?';
      form.action = '/';
      confirmButton.textContent = 'Sim, Sair';
    }
  });
});

