function deleteCategory(categoryId, csrfToken) {
  if (confirm("Ви впевнені, що хочете видалити цю категорію?")) {
    let url = `/category/${categoryId}/`;

    fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
    })
    .then(function(response) {
      if (response.ok) {
        let category = document.getElementById(`category-${categoryId}`);
        category.remove();
      } else {
        alert("Не вдалося видалити категорію.");
      }
    })
    .catch(function(error) {
      console.log(error);
      alert("Під час видалення категорії виникла помилка.");
    });
  }
}
