function deleteAccount(accountId, csrfToken) {
  if (confirm("Ви впевнені, що хочете видалити цей рахунок?")) {
    let url = `/account/${accountId}/`;

    fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
    })
    .then(function(response) {
      if (response.ok) {
        let account = document.getElementById(`account-${accountId}`);
        account.remove();
      } else {
        alert("Не вдалося видалити рахунок.");
      }
    })
    .catch(function(error) {
      console.log(error);
      alert("Під час видалення рахунку виникла помилка.");
    });
  }
}
