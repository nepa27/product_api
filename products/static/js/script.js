const form = document.getElementById('add-product-form');
const productListBody = document.getElementById('product-list-body');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const description = document.getElementById('description').value;
  const price = document.getElementById('price').value;

  fetch('http://localhost:8000/api/products/create/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, description, price })
  })
  .then(response => response.json())
  .then((data) => {
    console.log(data);
    updateProductList();
  })
  .catch((error) => {
    console.error(error);
  });
});

function updateProductList() {
  fetch('http://localhost:8000/api/products/')
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Error fetching products');
      }
    })
    .then((data) => {
      const productListHtml = data.map((product) => {
        return `
          <tr>
            <td>${product.name}</td>
            <td>${product.description}</td>
            <td>${product.price}</td>
          </tr>
        `;
      }).join('');
      productListBody.innerHTML = productListHtml;
    })
    .catch((error) => {
      console.error(error);
    });
}

updateProductList();
