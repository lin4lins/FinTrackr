const expenseBtn = document.getElementById('expense-btn');
const incomeBtn = document.getElementById('income-btn');

expenseBtn.addEventListener('click', () => {
  expenseBtn.classList.add('btn-danger');
  expenseBtn.classList.remove('btn-outline-danger');

  incomeBtn.classList.remove('btn-success');
  incomeBtn.classList.add('btn-outline-success');

  const expenseDivElement = document.getElementById('exp-category-div');
  expenseDivElement.style.display = 'block';
  const incomeDivElement = document.getElementById('inc-category-div');
  incomeDivElement.style.display = 'none';
});

incomeBtn.addEventListener('click', () => {
  incomeBtn.classList.remove('btn-outline-success');
  incomeBtn.classList.add('btn-success');

  expenseBtn.classList.remove('btn-danger');
  expenseBtn.classList.add('btn-outline-danger');

  const incomeDivElement = document.getElementById('inc-category-div');
  incomeDivElement.style.display = 'block';
  const expenseDivElement = document.getElementById('exp-category-div');
  expenseDivElement.style.display = 'none';
});
