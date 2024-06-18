const productsContainer = document.querySelector('.products');
const statsContainer = document.querySelector('.stats');

// Функция для загрузки товаров из базы данных
async function loadProducts() {
    const response = await fetch('/api/products');
    const data = await response.json();

    data.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');

        const imageElement = document.createElement('img');
        imageElement.src = product.image;
        productElement.appendChild(imageElement);

        const titleElement = document.createElement('h3');
        titleElement.textContent = product.title;
        productElement.appendChild(titleElement);

        const priceElement = document.createElement('p');
        priceElement.classList.add('price');
        const discount = product.discount ? ` (-${product.discount}%)` : '';
        priceElement.textContent = `${product.price} руб.${discount}`;
        productElement.appendChild(priceElement);

        productsContainer.appendChild(productElement);
    });
}

// Функция для загрузки статистики из базы данных
async function loadStats() {
    const response = await fetch('/api/stats');
    const data = await response.json();

    const ordersCountElement = statsContainer.querySelector('.orders-count');
    ordersCountElement.textContent = `Заказов: ${data.orders_count}`;

    const salesAmountElement = statsContainer.querySelector('.sales-amount');
    salesAmountElement.textContent = `Продаж: ${data.sales_amount} руб.`;
}

// Загрузка товаров и статистики
loadProducts();
loadStats();