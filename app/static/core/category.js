
function addExpenseCategory(csrfToken) {
  const url = '/category/';
  const headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken,
  };
  const categoryName = document.getElementById(`id_name`);
  let category_data = {'type': 'e', 'name': categoryName.value}

  fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(category_data)
  })
  .then(response => {
    if (response.status === 200) {
      let statusDiv = document.getElementById(`statusDiv-${subId}`);
        statusDiv.innerHTML = `<span class="badge rounded-pill" style="color: #00BF63; border: 1px solid #00BF63; background-color: #E5F8EF; margin-left: 5px;">✓ Completed</span>`
    }
  })
  .catch(error => console.error(error));
}
